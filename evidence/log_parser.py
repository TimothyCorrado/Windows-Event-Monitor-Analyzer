import re, collections

# Read file content
with open("FailedLogons.txt", "r", encoding="utf-8", errors="ignore") as f:
    data = f.read()

# Count total failed logons (case-insensitive)
total = len(re.findall(r"failed\s*to\s*log", data, re.IGNORECASE))

# Find all IPs (if any)
ips = re.findall(r'(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)', data)
ip_counts = collections.Counter(ips)

print("Top Failed Login Source IPs:")
if ip_counts:
    for ip, count in ip_counts.most_common():
        print(f"{ip}: {count} failed attempts")
else:
    print("(none found in this export — common if these are local logons)")

print(f"\nTotal failed logons: {total}")
