# Windows Event Monitor & Analyzer (Home Cyber Lab)

[![Status](https://img.shields.io/badge/status-active-brightgreen)]()
[![Made with Python](https://img.shields.io/badge/Python-3.x-blue)]()
[![PowerShell](https://img.shields.io/badge/PowerShell-✓-blue)]()
[![Wireshark](https://img.shields.io/badge/Wireshark-✓-blue)]()
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Kali%20%7C%20VirtualBox-lightgrey)]()

![Status](https://img.shields.io/badge/Status-All%20Phases%20Completed-brightgreen)
![Completion](https://img.shields.io/badge/Project%20Finalized-November%208%2C%202025-blue)
![Dashboard](https://img.shields.io/badge/HTML%20Dashboard-Generated%20Successfully-lightgrey)

> 🏁 **Final Status:** All six phases completed, verified, and documented — **Full-cycle Blue Team project:** from log collection and event correlation to automated anomaly detection and HTML dashboard visualization.

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
| 🧩 4 | Correlate network captures with event timestamps | 6 hrs | 2 hrs | ✅ Completed | Nov 7, 2025 |
| 🧩 5 | Document findings & write final report | 2 hrs | 1 hr | ✅ Completed | Nov 8, 2025 |
| 🧩 6 | Bonus: automation + HTML dashboard | 9 hrs | 2 hrs | ✅ Completed | Nov 8, 2025 |
| **🧾 Total** | **All Phases 1–6 Complete** | **41 hrs** | **18 hrs** | 🏁 **Project Complete** | Nov 8, 2025 |

> ⚡ **Completed Early:** Finished all 6 phases in 18 hours — roughly **56% faster** than estimated.

---

### 🗓️ Project Updates

## 🔹 Phase 6 — ✅ Completed  
**Implement Bonus Upgrades**  
**Date:** November 8, 2025  

**Summary**  
- Enhanced the Python parser to include **ratio-based anomaly detection**, comparing Windows Security **Event ID 4625 (Failed Logons)** vs. **4624 (Successful Logons)**.  
- Configured the script to flag failure ratios ≥ 30% as potential brute-force or password-spraying indicators.  
- Added an **HTML dashboard** that visualizes logon statistics (totals, top source IPs, and top targeted accounts).  
- Exported fresh Windows Security logs from host **TIMOT** for accurate testing:  
  - `wevtutil qe Security /q:"*[System[(EventID=4625)]]" /f:text > FailedLogons.txt`  
  - `wevtutil qe Security /q:"*[System[(EventID=4624)]]" /f:text > SuccessfulLogons.txt`  
- Parsed both exports successfully, identifying **24 failed logons** and **823 successful logons** (≈ 3% failure rate — normal bounds).  
- Verified failed attempts originated mainly from **127.0.0.1** (localhost) and **192.168.56.11** (Kali VM).  
- Confirmed that the **Tim** account was the top target during simulated RDP brute-force activity from Phase 4.  

**Deliverables**  
| File | Description |  
|------|--------------|  
| [`parser.py`](parser.py) | Final Python parser with anomaly-detection logic and HTML dashboard output |  
| [`FailedLogons.txt`](evidence/FailedLogons.txt) | Windows Security export — Event ID 4625 (Failed Logons) |  
| [`SuccessfulLogons.txt`](evidence/SuccessfulLogons.txt) | Windows Security export — Event ID 4624 (Successful Logons) |  
| [`log_summary.txt`](evidence/log_summary.txt) | Final parsed summary showing totals, top IPs, and failure ratio |  
| [`dashboard.html`](evidence/dashboard.html) | HTML visualization of parsed logon activity and indicators |  
| [`final_parser_run.png`](evidence/final_parser_run.png) | Screenshot of successful parser execution and summary output |  
| [`Dashboard_html.png`](evidence/Dashboard_html.png) | Screenshot of dashboard.html open in a browser |  

**Visualization**  
![final_parser_run.png](evidence/final_parser_run.png)
![Dashboard_html.png](evidence/Dashboard_html.png)

## 🔹 Phase 5 — ✅ Completed  
**Finalize Documentation & Repository Submission**  
**Date:** November 8, 2025  

**Summary**  
- Consolidated all project deliverables and verified each phase (1–4) was accurately documented in this README.  
- Ensured all evidence files (screenshots, reports, and parser outputs) were stored in the `/evidence` directory.  
- Reviewed the Python scripts for clarity, added inline comments, and confirmed successful parsing and reporting functionality.  
- Verified GitHub repository structure and updated README formatting for consistency across all phases.  
- Completed final commit and push to GitHub to finalize project submission.  

**Deliverables**  
- Updated `README.md` (Phases 1 – 5 complete)  

## 🔹 Phase 4 — ✅ Completed  
**Validate Network Context**  
**Date:** November 7, 2025  

**Summary**  
- Enabled Remote Desktop Protocol (RDP) on the Windows VM and confirmed connectivity between Kali (`192.168.56.11`) and Windows (`192.168.56.10`).  
- Started Wireshark on both Kali and Windows to monitor TCP **3389** (RDP) traffic.  
- Generated multiple failed RDP logon attempts from Kali using `xfreerdp3` to simulate brute-force activity.  
- Captured and saved both network traces as `.pcapng` files for later analysis.  
- Applied the display filter `ip.addr == 192.168.56.10 && tcp.port == 3389` to isolate the RDP handshake and authentication packets.  
- Verified that the timestamps in Wireshark align with Windows Security **Event ID 4625** entries.

**Deliverables**  
| File | Description |  
|------|--------------|  
| [`kali_failedlogons_Phase4.pcapng`](evidence/kali_failedlogons_Phase4.pcapng) | Network capture of failed RDP attempts from Kali → Windows (TCP 3389) |  
| [`windows_failedlogons_Phase4.pcapng`](evidence/windows_failedlogons_Phase4.pcapng) | Corresponding capture from Windows endpoint showing inbound RDP traffic |  
| [`Windows_Kali_FailedLogs_Phase4.png`](evidence/Windows_Kali_FailedLogs_Phase4.png) | Screenshot of Wireshark (Kali & Windows) filtered on TCP 3389 with visible timestamps & IPs 

**Visualization**  
![Windows_Kali_FailedLogs_Phase4.png](evidence/Windows_Kali_FailedLogs_Phase4.png)   

## 🔹 Phase 3 — ✅ Completed  
**Build the Python Log Parser**  
**Date:** November 6, 2025  

**Summary**  
- Exported failed-logon events (4625) from Windows to a text file and copy it into the repo: `evidence/FailedLogons.txt`.  
- Opened the parser (`evidence/log_parser.py`) and ensure it reads `FailedLogons.txt` with UTF-8 encoding.  
- Ran the script on Kali/terminal to parse the file and detect failed authentication attempts using regex.  
- Generated a summary report with total failed logons and top source IPs; save as `evidence/log_summary.txt`.  
- Captured proof of a successful run (terminal output showing totals/IPs) and save the screenshot as `evidence/log_parser_running.png`.  

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

#### 🧩 Phase 4 – Correlate Network Captures with Event Timestamps
- Captured and analyzed **Wireshark network traces** from both Kali and Windows during simulated RDP logon attempts.  
- Applied targeted filters (`ip.addr == 192.168.56.10 && tcp.port == 3389`) to isolate **RDP handshake and authentication traffic**.  
- Correlated Wireshark timestamps with Windows Security **Event ID 4625** entries to confirm event accuracy.  
- Validated that the RDP attack from **Kali (192.168.56.11)** directly caused failed logon events on **Windows (192.168.56.10)**.  
- Reinforced understanding of how **network and host-level logs interrelate** in security investigations.  

#### 🧩 Phase 5 – Document Findings & Finalize Report
- Consolidated all **evidence files, screenshots, and scripts** into a structured GitHub repository.  
- Documented each project phase in **README.md** with consistent formatting, summaries, and deliverable tables.  
- Learned the importance of **traceability and reproducibility** in security research projects.  
- Practiced writing **clear technical documentation** suitable for SOC reports or project submissions.  
- Gained confidence in using GitHub for professional-grade version control and evidence presentation.  

#### 🧩 Phase 6 – Implement Bonus Upgrades
- Expanded the Python parser with **ratio-based anomaly detection**, calculating failed vs. successful logon ratios.  
- Implemented **alert thresholds** (≥30% failure ratio) to flag potential brute-force or password-spraying attempts.  
- Added an automated **HTML dashboard generator** for visual triage of top IPs, targeted accounts, and totals.  
- Resolved **UTF-16 encoding issues** when reading Windows log exports, ensuring accurate event parsing.  
- Successfully detected **24 failed logons** vs. **823 successful logons**, confirming realistic network behavior.  
- Completed full project automation — from log collection to visualization — demonstrating end-to-end blue-team analysis.  


### 🏁 Final Reflection  

This project provided hands-on experience across the **entire incident analysis lifecycle** — from data collection to automation and visualization. Each phase reinforced key cybersecurity fundamentals:  

- **Phase 1–2** built a realistic, sandboxed environment where I simulated adversarial activity and captured genuine log artifacts.  
- **Phase 3** transformed those raw events into structured, queryable data through Python scripting and regex-based parsing.  
- **Phase 4** demonstrated how to correlate **network traffic (Wireshark)** with **host-based evidence (Event IDs)** to prove event causality.  
- **Phase 5** focused on documentation, GitHub workflow, and version control — reinforcing that strong technical work must also be **well-communicated**.  
- **Phase 6** elevated the project with automation and visualization, turning a static report into a **dynamic, repeatable tool** that mirrors real-world blue team workflows.  

By the end, I had developed not just a functioning parser and dashboard, but also a **repeatable SOC-style pipeline** for detecting, validating, and reporting authentication anomalies.  
This project strengthened my technical, analytical, and communication skills.  

## 🏁 Final Resume Line
> Windows Event Log Analyzer (Cybersecurity Home Lab Project) – Designed and built a hands-on SOC simulation lab using Windows and Kali Linux. Collected and analyzed Windows Security Event Logs (Event ID 4625) to identify failed authentication attempts, automated log parsing with Python and PowerShell, and correlated findings with Wireshark network captures to demonstrate real-world incident detection and response workflows.

<!--

listing this project on my résumé or LinkedIn, format it like this:

Windows Event Log Analyzer (Cybersecurity Home Lab Project) | GitHub: github.com/TimothyCorrado/Windows-Event-Monitor-Analyzer  
- Built a virtual SOC lab using Windows and Kali Linux to simulate blue-team workflows.  
- Collected and analyzed Security Event Logs (Event ID 4625) to identify failed logons.  
- Automated log parsing and reporting using Python and PowerShell.  
- Correlated system events with Wireshark network captures for incident validation.-->