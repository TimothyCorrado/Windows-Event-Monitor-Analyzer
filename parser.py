import argparse, os, re
from collections import Counter
from datetime import datetime

# More forgiving patterns: match anywhere in the line, ignore case
EVENT_HEADER_RE = re.compile(r'Event ID:\s*(\d+)', re.IGNORECASE)
DATETIME_RE = re.compile(r'Date:\s*(.+)', re.IGNORECASE)
ACCOUNT_NAME_RE = re.compile(r'Account Name:\s*(.+)', re.IGNORECASE)
TARGET_NAME_RE = re.compile(r'User Name:\s*(.+)', re.IGNORECASE)
SRC_IP_RE = re.compile(r'Source Network Address:\s*(.+)', re.IGNORECASE)
IP_INLINE_RE = re.compile(
    r'(?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d)'
)

def parse_wevtutil_text(path):
    """
    Parse a Windows Event Log exported with:
      wevtutil qe Security /q:"*[System[(EventID=4625)]]" /f:text
    or the same with 4624.
    Splits events by lines starting with 'Event['.
    """
    events = []
    with open(path, "r", encoding="utf-16", errors="ignore") as f:
        block = []
        for line in f:
            if line.startswith("Event[") and block:
                ev = parse_block(block)
                if ev:
                    events.append(ev)
                block = [line.rstrip("\n")]
            else:
                block.append(line.rstrip("\n"))
        # last block
        if block:
            ev = parse_block(block)
            if ev:
                events.append(ev)
    return events

def parse_block(lines):
    """Extract event_id, timestamp, account, and src_ip from one event block."""
    ev = {'event_id': None, 'when': None, 'account': None, 'src_ip': None}

    for ln in lines:
        ln = ln.rstrip("\r\n")

        # Event ID (4624 / 4625)
        m = EVENT_HEADER_RE.search(ln)
        if m:
            ev['event_id'] = m.group(1)

        # Date / time
        m = DATETIME_RE.search(ln)
        if m and not ev['when']:
            ev['when'] = m.group(1).strip()

        # Source IP
        m = SRC_IP_RE.search(ln)
        if m and not ev['src_ip']:
            cand = m.group(1).strip()
            ip = IP_INLINE_RE.search(cand)
            if ip:
                ev['src_ip'] = ip.group(0)
            else:
                ev['src_ip'] = None if cand == '-' else cand

        # Account Name (user)
        m = ACCOUNT_NAME_RE.search(ln)
        if m:
            candidate = m.group(1).strip()
            # Prefer non-N/A and override machine accounts ending with $
            if (not ev['account']
                or ev['account'].upper() == 'N/A'
                or ev['account'].endswith('$')):
                ev['account'] = candidate

        # Sometimes "User Name" is used
        m = TARGET_NAME_RE.search(ln)
        if m and not ev['account']:
            ev['account'] = m.group(1).strip()

        # Fallback inline IP search
        if not ev['src_ip']:
            ip2 = IP_INLINE_RE.search(ln)
            if ip2:
                ev['src_ip'] = ip2.group(0)

    # Only keep the logon events we care about
    return ev if ev.get('event_id') in ('4624', '4625') else None

def summarize(events):
    failed = [e for e in events if e['event_id'] == '4625']
    success = [e for e in events if e['event_id'] == '4624']

    def count_by(items, key):
        return Counter((i.get(key) or 'UNKNOWN') for i in items)

    return {
        'failed_total': len(failed),
        'success_total': len(success),
        'failed_by_ip': count_by(failed, 'src_ip'),
        'failed_by_user': count_by(failed, 'account'),
        'success_by_user': count_by(success, 'account'),
    }

def fmt(counter, title):
    lines = [title]
    for item, cnt in counter.most_common(10):
        lines.append(f"  - {item}: {cnt}")
    return "\n".join(lines) + "\n"

def generate_html_dashboard(summary, out_path):
    """Generate a simple HTML dashboard showing logon stats."""
    failed_total = summary['failed_total']
    success_total = summary['success_total']

    def counter_to_rows(counter):
        rows = []
        for item, cnt in counter.most_common(10):
            rows.append(f"<tr><td>{item}</td><td>{cnt}</td></tr>")
        return "\n".join(rows)

    html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Windows Logon Triage Dashboard</title>
</head>
<body>
  <h1>Windows Logon Triage Dashboard</h1>

  <h2>Totals</h2>
  <p><strong>Failed logons (4625):</strong> {failed_total}</p>
  <p><strong>Successful logons (4624):</strong> {success_total}</p>

  <h2>Top Source IPs (Failed 4625)</h2>
  <table border="1" cellpadding="4">
    <tr><th>Source IP</th><th>Count</th></tr>
    {counter_to_rows(summary['failed_by_ip'])}
  </table>

  <h2>Top Targeted Accounts (Failed 4625)</h2>
  <table border="1" cellpadding="4">
    <tr><th>Account</th><th>Count</th></tr>
    {counter_to_rows(summary['failed_by_user'])}
  </table>

  <h2>Top Accounts (Successful 4624)</h2>
  <table border="1" cellpadding="4">
    <tr><th>Account</th><th>Count</th></tr>
    {counter_to_rows(summary['success_by_user'])}
  </table>
</body>
</html>
"""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

def main():
    ap = argparse.ArgumentParser(description="Parse wevtutil text exports for 4625/4624 triage.")
    ap.add_argument("--failed", help="Path to FailedLogons.txt")
    ap.add_argument("--success", help="Path to SuccessfulLogons.txt")
    ap.add_argument("--out", help="Write report to this path (optional)")
    args = ap.parse_args()

    events = []
    if args.failed and os.path.exists(args.failed):
        events += parse_wevtutil_text(args.failed)
    if args.success and os.path.exists(args.success):
        events += parse_wevtutil_text(args.success)

    summary = summarize(events)

    # Ratio-based anomaly detection
    failed = summary['failed_total']
    success = summary['success_total']
    if success > 0:
        fail_ratio = failed / success
        if fail_ratio > 0.3:
            ratio_note = f"ALERT: High failure ratio detected ({fail_ratio:.2f}). Possible brute-force or password spraying."
        else:
            ratio_note = f"Failure ratio is {fail_ratio:.2f}, within normal bounds."
    else:
        if failed > 0:
            ratio_note = "ALERT: Failed logons detected with no successful logons recorded."
        else:
            ratio_note = "No logon activity detected."

    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%SZ')
    report = []
    report.append("Windows Logon Triage Summary")
    report.append(f"Generated: {now} UTC\n")
    report.append(f"Total failed logons (4625): {summary['failed_total']}")
    report.append(f"Total successful logons (4624): {summary['success_total']}\n")
    report.append(ratio_note + "\n")
    report.append(fmt(summary['failed_by_ip'], "Top source IPs (failed 4625):"))
    report.append(fmt(summary['failed_by_user'], "Top targeted accounts (failed 4625):"))
    report.append(fmt(summary['success_by_user'], "Top accounts (successful 4624):"))
    report.append("Notes:")
    report.append("  • Investigate IPs with unusually high failed attempts.")
    report.append("  • Compare failed vs. successful to spot possible compromises.")
    report.append("  • Align timestamps with Wireshark or firewall logs for deeper correlation.\n")

    report_text = "\n".join(report)
    print(report_text)

    # Write HTML dashboard
    html_path = os.path.join("evidence", "dashboard.html")
    try:
        generate_html_dashboard(summary, html_path)
        print(f"\n[+] HTML dashboard written to {html_path}")
    except Exception as e:
        print(f"[!] Failed to write HTML dashboard: {e}")

    # Optionally write plain-text report
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(report_text)

if __name__ == "__main__":
    main()