#!/usr/bin/env python3
# A lightweight Windows Security log triage script.
# - Parses wevtutil text exports for Event IDs 4625 (failed) and 4624 (successful).
# - Summarizes by source IP and by account name.
# - Writes a plain-text report to stdout and optionally to a file.
import argparse, os, re
from collections import Counter
from datetime import datetime

EVENT_HEADER_RE = re.compile(r'^\s*Event ID:\s*(\d+)\s*$')
DATETIME_RE = re.compile(r'^\s*Date:\s*(.+)$', re.IGNORECASE)
ACCOUNT_NAME_RE = re.compile(r'^\s*Account Name:\s*(.+)$', re.IGNORECASE)
TARGET_NAME_RE = re.compile(r'^\s*User Name:\s*(.+)$', re.IGNORECASE)
SRC_IP_RE = re.compile(r'^\s*Source Network Address:\s*(.+)$', re.IGNORECASE)
IP_INLINE_RE = re.compile(r'(?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d)')

def parse_wevtutil_text(path):
    events = []
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        block = []
        for line in f:
            if line.strip() == "":
                if block:
                    ev = parse_block(block)
                    if ev: events.append(ev)
                    block = []
            else:
                block.append(line.rstrip("\n"))
        if block:
            ev = parse_block(block)
            if ev: events.append(ev)
    return events

def parse_block(lines):
    ev = {'event_id': None, 'when': None, 'account': None, 'src_ip': None}
    for ln in lines:
        m = EVENT_HEADER_RE.match(ln)
        if m: ev['event_id'] = m.group(1)
        m = DATETIME_RE.match(ln)
        if m and not ev['when']: ev['when'] = m.group(1).strip()
        m = SRC_IP_RE.match(ln)
        if m and not ev['src_ip']:
            cand = m.group(1).strip()
            ip = IP_INLINE_RE.search(cand)
            ev['src_ip'] = ip.group(0) if ip else (None if cand == '-' else cand)
        m = ACCOUNT_NAME_RE.match(ln)
        if m and not ev['account']: ev['account'] = m.group(1).strip()
        m = TARGET_NAME_RE.match(ln)
        if m and not ev['account']: ev['account'] = m.group(1).strip()
        if not ev['src_ip']:
            ip2 = IP_INLINE_RE.search(ln)
            if ip2: ev['src_ip'] = ip2.group(0)
    return ev if ev.get('event_id') in ('4625','4624') else None

def summarize(events):
    failed = [e for e in events if e['event_id']=='4625']
    success = [e for e in events if e['event_id']=='4624']
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
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%SZ')
    report = []
    report.append("Windows Logon Triage Summary")
    report.append(f"Generated: {now} UTC\n")
    report.append(f"Total failed logons (4625): {summary['failed_total']}")
    report.append(f"Total successful logons (4624): {summary['success_total']}\n")
    report.append(fmt(summary['failed_by_ip'], "Top source IPs (failed 4625):"))
    report.append(fmt(summary['failed_by_user'], "Top targeted accounts (failed 4625):"))
    report.append(fmt(summary['success_by_user'], "Top accounts (successful 4624):"))
    report.append("Notes:\n  • Investigate IPs with unusually high failed attempts.\n  • Compare failed vs. successful to spot compromised credentials.\n  • Align timestamps with Wireshark captures for correlation.\n")
    report_text = "\n".join(report)

    print(report_text)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(report_text)

if __name__ == "__main__":
    main()
