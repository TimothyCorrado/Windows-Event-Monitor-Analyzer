# Windows Event Monitor & Analyzer (Home Cyber Lab)

[![Status](https://img.shields.io/badge/status-active-brightgreen)]()
[![Made with Python](https://img.shields.io/badge/Python-3.x-blue)]()
[![PowerShell](https://img.shields.io/badge/PowerShell-✓-blue)]()
[![Wireshark](https://img.shields.io/badge/Wireshark-✓-blue)]()
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Kali%20%7C%20VirtualBox-lightgrey)]()

![Status](https://img.shields.io/badge/Status-Phase%203%20Completed-brightgreen)
![Next](https://img.shields.io/badge/Next%20Up-Phase%204-blue)

### 🔍 Project Overview
Built a complete home cyber lab using **Windows 10 and Kali Linux** inside **VirtualBox** to collect, analyze, and correlate Windows Security Event Logs.  
The project demonstrates end-to-end blue-team workflow skills — from log collection and parsing to network validation and final reporting — using real tools such as **PowerShell, Python, and Wireshark**.

> 🛡️Hands-on cybersecurity project demonstrating event-log analysis, Python automation, and network correlation in a home virtual lab environment.

### 🕒 Project Timeline
| Phase | Focus | Est. Hours | Hours Spent | Status | Completed |
|-|-|-|-|-|-|
| 🧩 1 | Build virtual lab (Windows + Kali setup, networking, Wireshark test) | 9 hrs | 6 hrs | ✅ Completed | Nov 2, 2025 |
| 🧩 2 | Collect Windows Event Logs (PowerShell export) | 6 hrs | 4 hrs | ✅ Completed | Nov 5, 2025 |
| 🧩 3 | Develop Python log parser for failed logons | 9 hrs | 3 hrs | ✅ Completed | Nov 6, 2025 |
| 🧩 4 | Correlate network captures with event timestamps | 6 hrs | TBD | 🔄 In Progress | — |
| 🧩 5 | Document findings & write final report | 6 hrs | TBD | ⏳ Planned | — |
| 🧩 6 | Bonus: automation + HTML dashboard | Optional | TBD | 💡 Future Idea | — |
| **🧾 Total** | **Phases 1–3 Complete** | **36 hrs** | **13 hrs** | ✅ On Track | — |
> ⚡ **Ahead of Schedule:** Completed 3 phases in 13 hours — roughly 45% faster than estimated.

---

### 🗓️ Project Updates

## 🔹 Phase 3 — ✅ Completed  
**Build the Python Log Parser**  
**Date:** November 6, 2025  

**Summary**  
- Exported failed-logon events (4625) from Windows to a text file and copy it into the repo: `evidence/FailedLogons.txt`.  
- Opened the parser (`evidence/log_parser.py`) and ensure it reads `FailedLogons.txt` with UTF-8 encoding.  
- Ran the script on Kali/terminal to parse the file and detect failed authentication attempts using regex.  
- Generated a summary report with total failed logons and top source IPs; save as `evidence/log_summary.txt`.  
- Captured proof of a successful run (terminal output showing totals/IPs) and save the screenshot as `evidence/log_parser_running.png`.  
- Committed & pushed all Phase 3 artifacts to GitHub (script, summary, screenshot) and update this README section.

**Deliverables**
| File | Description |
|------|--------------|
| [`FailedLogons.txt`](evidence/FailedLogons.txt) | Raw exported Windows Security log (UTF-8 format) |
| [`log_parser.py`](evidence/log_parser.py) | Python 3 script used to parse and analyze failed logons |
| [`log_summary.txt`](evidence/log_summary.txt) | Text summary of total failed logons and top IP sources |
| [`log_parser_running.png`](evidence/log_parser_running.png) | Screenshot showing the successful Python run in Kali |

**Visualization**  
![log_parser_running.png](evidence/log_parser_running.png)  

## 🔹 Phase 2 — ✅ Completed  
**Collect & Analyze Windows Event Logs**  
**Date:** November 5, 2025  

**Summary**
- Enabled logon auditing and generated realistic 4625 events
- Exported full Windows Security log (.evtx) + filtered CSV + text + screenshot evidence
- Transferred data to Kali Linux for analysis via shared folders
- Parsed and summarized failed logons using Python (pandas + collections)
- Created visualizations (Matplotlib) showing logon failures by user and by hour

**Deliverables**
| File | Description |
|------|--------------|
| [`Failed_Logons.csv`](evidence/Failed_Logons.csv) | Raw failed-logon events |
| [`SecurityLogs_Full.evtx`](evidence/SecurityLogs_Full.evtx) | Full Windows Security log export |
| [`FailedLogons.txt`](evidence/FailedLogons.txt) | Text summary of PowerShell output |
| [`FailedLogons_Screenshot.png`](evidence/FailedLogons_Screenshot.png) | Proof of PowerShell export |
| [`failed_logon_summary.txt`](evidence/failed_logon_summary.txt) | Kali analysis summary |
| [`failed_logons_by_user.png`](evidence/failed_logons_by_user.png) | Visualization – failed logons by user |
| [`failed_logons_by_hour.png`](evidence/failed_logons_by_hour.png) | Visualization – failed logons by hour |

## 🔹 Phase 1 — ✅ Completed  
**Build Your Home Cyber Lab**  
**Date:** November 4, 2025  

**Summary:**  
- Created two virtual machines (Windows 10 + Kali Linux) in VirtualBox.  
- Configured an **Internal Network** named `CyberLabNet`.  
- Verified connectivity with ICMP (ping) tests.  
- Captured traffic in Wireshark and saved evidence.

**Visualization**  
![Lab Setup Screenshot](evidence/lab_setup.png)  
[Wireshark Capture (lab_setup.pcapng)](evidence/lab_setup.pcapng)

## 🔹 Phase 1 — ✅ In Progress  
**Build Your Home Cyber Lab**  
**Date:** November 3, 2025  

**Summary:**
- Installed **VirtualBox**
- Downloaded **Kali Linux ISO (installer)** and **Windows 10 ISO**
- Created two virtual machines:
  - Kali Linux (4GB RAM, 20GB Disk)
  - Windows 10 (4GB RAM, 40GB Disk)
- Configured both on an **Internal Network** (`CyberLabNet`)
- Began testing connectivity (Wireshark + ping)

**Current Results**
- Kali and Windows both installed successfully
- Wireshark running and ready to capture packets
- Encountered minor network communication issues (to fix next session)

## 🧠 Key Takeaways

#### 🧩 Phase 1 – Build the Virtual Lab
- Learned how to configure **Windows and Kali Linux in VirtualBox** with internal networking for isolated testing.
- Practiced setting up **secure file sharing** between systems for evidence collection.
- Validated **network communication and packet visibility** using Wireshark to confirm traffic capture between virtual machines.
- Gained hands-on familiarity with how a real SOC might segment and monitor internal traffic in a sandboxed environment.

#### 🧩 Phase 2 – Collect Windows Event Logs
- Used **PowerShell (`wevtutil`)** to query and export Security Event Logs filtered by **Event ID 4625** (failed logons).
- Learned the difference between **Event IDs 4624 (successful logon)** and **4625 (failed logon)** and their relevance in brute-force detection.
- Understood **Windows event structure** — timestamp, source IP, account name, and logon type fields.
- Practiced exporting data in both **text and CSV formats**, and learned about **UTF-16 vs UTF-8 encoding** when transferring logs between Windows and Linux.

#### 🧩 Phase 3 – Develop the Python Log Parser
- Built a **custom Python script** (`log_parser.py`) to automate analysis of exported logs.
- Utilized **regex (regular expressions)** to match Event ID 4625 entries and extract IP addresses.
- Implemented **data aggregation with Python’s `collections.Counter`** to identify top failed login sources.
- Overcame file encoding issues, learned **error handling (`errors='ignore'`)**, and confirmed UTF-8 parsing in Linux.
- Created a **summary output file** and visual proof (terminal screenshot) — demonstrating data-driven log analysis from start to finish.

## 🏁 Final Resume Line
> Windows Event Log Analyzer (Cybersecurity Home Lab Project) – Designed and built a hands-on SOC simulation lab using Windows and Kali Linux. Collected and analyzed Windows Security Event Logs (Event ID 4625) to identify failed authentication attempts, automated log parsing with Python and PowerShell, and correlated findings with Wireshark network captures to demonstrate real-world incident detection and response workflows.

<!--

listing this project on my résumé or LinkedIn, format it like this:

Windows Event Log Analyzer (Cybersecurity Home Lab Project) | GitHub: github.com/TimothyCorrado/Windows-Event-Monitor-Analyzer  
- Built a virtual SOC lab using Windows and Kali Linux to simulate blue-team workflows.  
- Collected and analyzed Security Event Logs (Event ID 4625) to identify failed logons.  
- Automated log parsing and reporting using Python and PowerShell.  
- Correlated system events with Wireshark network captures for incident validation.-->