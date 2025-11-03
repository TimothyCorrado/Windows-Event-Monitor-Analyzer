# Windows Event Monitor & Analyzer (Home Cyber Lab Project)

**Goal:** Detect and summarize unusual Windows logon activity using **PowerShell + Python**, and correlate with **Wireshark** network captures — all inside a **VirtualBox** home lab (Windows + Kali).

## Stack
- **Virtualization:** VirtualBox (Windows 10/11 VM + Kali/Ubuntu VM)
- **OS/Tools:** Windows Event Viewer, PowerShell, Python 3, Wireshark, Kali Linux
- **Learning Platforms:** TryHackMe (optional validation labs)

## What this project demonstrates
- Windows **security auditing** and log export
- **Python** parsing of Event IDs **4625** (failed) and **4624** (successful) logons
- Per-IP and per-user **triage summaries** (find brute-force patterns)
- **Wireshark** packet capture correlation (e.g., RDP/SMB attempts)
- Clear **reporting** of findings and mitigations

## Quick start
1) **Export Windows Security logs** (failed & successful logons) via PowerShell:
   ```powershell
   # Failed logons (4625)
   wevtutil qe Security /q:"*[System[(EventID=4625)]]" /f:text > FailedLogons.txt
   # Successful logons (4624)
   wevtutil qe Security /q:"*[System[(EventID=4624)]]" /f:text > SuccessfulLogons.txt
   ```
   Place exported files in `./logs/`.

2) **(Optional) Capture network traffic** in Wireshark while generating logons.
   Save screenshots/pcaps in `./evidence/`.

3) **Run the parser** from this folder:
   ```bash
   python3 parser.py --failed ./logs/FailedLogons.txt --success ./logs/SuccessfulLogons.txt --out ./evidence/triage.txt
   ```

4) Review **`./evidence/triage.txt`** and add the most relevant screenshot(s) to your incident report.

## Example questions this project answers
- Which **IP addresses** produced the most failed logons?
- Which **usernames** were targeted?
- What was the **failed vs successful** ratio over the sample?
- Do **Wireshark timestamps** line up with the surge in failures?

## Suggested lab flow (match résumé bullets)
1. Build VirtualBox lab (Windows + Kali, host-only or NAT).
2. Configure security auditing; generate a handful of failed logons (test account).
3. Export logs; run `parser.py` to summarize anomalies.
4. Capture traffic in Wireshark during the test; add correlation notes.
5. Write a 1–2 page incident report from the template in `/report/`.
6. Push README, script, and evidence to GitHub (pin this repo).

## Next steps (roadmap)
- Automate Windows log export with Task Scheduler + PowerShell.
- Extend parser to include **4688** (process creation) and **4648** (logon with explicit credentials).
- Output an **HTML** summary with charts.
- (Optional) Forward logs into **Wazuh** or **Splunk Free** and tune a correlation rule.

## Screenshots / Evidence
- `./evidence/lab_setup.png`
- `./evidence/wireshark_failedlogons.png`
- `./evidence/triage.txt`

## Responsible AI Note
Portions of the structure and code were drafted with assistance from AI tools for productivity. All steps were executed, tested, and documented by me to ensure full understanding of the implementation and findings.
