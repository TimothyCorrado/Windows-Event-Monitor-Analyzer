"""
parser.py — Windows Event Log Parser
------------------------------------
This script parses Windows Security Event logs exported with `wevtutil`,
specifically focusing on:

    • Event ID 4625 → Failed logons
    • Event ID 4624 → Successful logons

It extracts key details (timestamp, username, source IP), summarizes them,
and outputs a report showing failed attempts, top IPs, and top users.
"""

# --- IMPORTS ---
# These modules give us text parsing, counting, and command-line handling tools.
import argparse           # For handling command-line arguments (e.g. --failed --success)
import os                 # For checking file paths and existence
import re                 # For regular expressions (pattern matching in text)
from collections import Counter  # For counting frequency of items (like IPs or usernames)
from datetime import datetime    # For adding timestamps to the report

# --- REGEX PATTERNS ---
# These help locate and extract specific pieces of text from each event block.
# Example of event text lines being matched:
#   Event ID: 4625
#   Date: 2025-11-08 13:42:15
#   Account Name: tim
#   Source Network Address: 192.168.1.15

EVENT_HEADER_RE = re.compile(r'^\s*Event ID:\s*(\d+)\s*$')
DATETIME_RE = re.compile(r'^\s*Date:\s*(.+)$', re.IGNORECASE)
ACCOUNT_NAME_RE = re.compile(r'^\s*Account Name:\s*(.+)$', re.IGNORECASE)
TARGET_NAME_RE = re.compile(r'^\s*User Name:\s*(.+)$', re.IGNORECASE)
SRC_IP_RE = re.compile(r'^\s*Source Network Address:\s*(.+)$', re.IGNORECASE)

# This pattern matches any IPv4 address, even if embedded in a line.
IP_INLINE_RE = re.compile(
    r'(?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d)'
)


# --- FUNCTION 1: parse_wevtutil_text() ---
# Reads a text file exported from Windows Event Viewer, splits it into
# individual events (each separated by blank lines), and parses each one.

def parse_wevtutil_text(path):
    events = []  # This will hold our parsed events (each one a dict)
    
    # Open the log text file safely using UTF-8 encoding
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        block = []  # Temporary list to store lines of one event block

        # Read each line from the file
        for line in f:
            # A blank line means one event block has ended
            if line.strip() == "":
                # Only parse if we actually have lines collected
                if block:
                    ev = parse_block(block)  # Turn those lines into an event dictionary
                    if ev:  # Only add it if valid
                        events.append(ev)
                    block = []  # Reset for the next event
            else:
                # Still within an event block — keep adding lines
                block.append(line.rstrip("\n"))

        # Handle last block if file didn’t end with a blank line
        if block:
            ev = parse_block(block)
            if ev:
                events.append(ev)
    
    return events  # Returns a list of dicts, one per event


# --- FUNCTION 2: parse_block() ---
# Takes one "event block" (list of lines) and extracts key details
# using the regex patterns defined above.

def parse_block(lines):
    # Start with an empty dictionary to hold event data
    ev = {
        'event_id': None,
        'when': None,
        'account': None,
        'src_ip': None
    }

    # Go line by line through the event block
    for ln in lines:
        # Match Event ID (e.g. 4625)
        m = EVENT_HEADER_RE.match(ln)
        if m:
            ev['event_id'] = m.group(1)

        # Match Date/Time
        m = DATETIME_RE.match(ln)
        if m and not ev['when']:
            ev['when'] = m.group(1).strip()

        # Match Source IP address
        m = SRC_IP_RE.match(ln)
        if m and not ev['src_ip']:
            cand = m.group(1).strip()
            # Try to find a proper IP within the line
            ip = IP_INLINE_RE.search(cand)
            if ip:
                ev['src_ip'] = ip.group(0)
            else:
                # If it says '-', treat as no IP
                ev['src_ip'] = None if cand == '-' else cand

        # Match Account Name (user)
        m = ACCOUNT_NAME_RE.match(ln)
        if m and not ev['account']:
            ev['account'] = m.group(1).strip()

        # Sometimes "User Name" is used instead of "Account Name"
        m = TARGET_NAME_RE.match(ln)
        if m and not ev['account']:
            ev['account'] = m.group(1).strip()

        # If still no src_ip found, try to spot one inline anywhere in the line
        if not ev['src_ip']:
            ip2 = IP_INLINE_RE.search(ln)
            if ip2:
                ev['src_ip'] = ip2.group(0)

    # Return only if it’s an event we care about (4624 or 4625)
    return ev if ev.get('event_id') in ('4624', '4625') else None


# --- FUNCTION 3: summarize() ---
# Takes all parsed events and counts totals by type, IP, and username.

def summarize(events):
    # Separate successful and failed logon events
    failed = [e for e in events if e['event_id'] == '4625']
    success = [e for e in events if e['event_id'] == '4624']

    # Helper: counts occurrences of a chosen key (e.g., IP or account)
    def count_by(items, key):
        # Default to 'UNKNOWN' if missing
        return Counter((i.get(key) or 'UNKNOWN') for i in items)

    # Return a summary dictionary
    return {
        'failed_total': len(failed),
        'success_total': len(success),
        'failed_by_ip': count_by(failed, 'src_ip'),
        'failed_by_user': count_by(failed, 'account'),
        'success_by_user': count_by(success, 'account'),
    }


# --- FUNCTION 4: fmt() ---
# Turns a Counter (like top IPs) into a nicely formatted text list.

def fmt(counter, title):
    lines = [title]  # First line = section header (e.g. "Top source IPs")
    # Show top 10 entries from the counter
    for item, cnt in counter.most_common(10):
        lines.append(f"  - {item}: {cnt}")
    return "\n".join(lines) + "\n"


# --- FUNCTION 5: main() ---
# This ties everything together and runs when you execute the script.

def main():
    # Create argument parser for command-line use
    ap = argparse.ArgumentParser(description="Parse wevtutil text exports for 4625/4624 triage.")
    ap.add_argument("--failed", help="Path to FailedLogons.txt")
    ap.add_argument("--success", help="Path to SuccessfulLogons.txt")
    ap.add_argument("--out", help="Write report to this path (optional)")
    args = ap.parse_args()

    events = []  # will hold all events combined

    # If user provided a path to failed logs, parse it
    if args.failed and os.path.exists(args.failed):
        events += parse_wevtutil_text(args.failed)

    # If user provided a path to successful logs, parse it
    if args.success and os.path.exists(args.success):
        events += parse_wevtutil_text(args.success)

    # Generate the statistical summary
    summary = summarize(events)

    # Timestamp for report
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%SZ')

    # Build the report text line-by-line
    report = []
    report.append("Windows Logon Triage Summary")
    report.append(f"Generated: {now} UTC\n")
    report.append(f"Total failed logons (4625): {summary['failed_total']}")
    report.append(f"Total successful logons (4624): {summary['success_total']}\n")

    # Add sections for top IPs and accounts
    report.append(fmt(summary['failed_by_ip'], "Top source IPs (failed 4625):"))
    report.append(fmt(summary['failed_by_user'], "Top targeted accounts (failed 4625):"))
    report.append(fmt(summary['success_by_user'], "Top accounts (successful 4624):"))

    # Add final analysis notes
    report.append("Notes:")
    report.append("  • Investigate IPs with unusually high failed attempts.")
    report.append("  • Compare failed vs. successful to spot possible compromises.")
    report.append("  • Align timestamps with Wireshark or firewall logs for deeper correlation.\n")

    # Join all parts into one text string
    report_text = "\n".join(report)

    # Display report in terminal
    print(report_text)

    # Optionally write to a file if --out was specified
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(report_text)


# --- ENTRY POINT ---
# This ensures the script only runs `main()` if executed directly,
# not if imported as a module.
if __name__ == "__main__":
    main()