# Windows Event Monitor & Analyzer (Home Cyber Lab)

[![Status](https://img.shields.io/badge/status-active-brightgreen)]()
[![Made with Python](https://img.shields.io/badge/Python-3.x-blue)]()
[![PowerShell](https://img.shields.io/badge/PowerShell-✓-blue)]()
[![Wireshark](https://img.shields.io/badge/Wireshark-✓-blue)]()
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Kali%20%7C%20VirtualBox-lightgrey)]()

![Status](https://img.shields.io/badge/Status-Phase%203%20Completed-brightgreen)
![Next](https://img.shields.io/badge/Next%20Up-Phase%204%20Planned-blue)

Detect and summarize unusual Windows logon activity using **PowerShell + Python**, and correlate with **Wireshark** network captures — all inside a **VirtualBox** home lab (Windows + Kali).

> **Hiring managers:** This project simulates a junior SOC workflow: collect → parse → triage → correlate → report.

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

**Visualization**  
![Failed Logons by User](evidence/failed_logons_by_user.png)  
![Failed Logons by Hour](evidence/failed_logons_by_hour.png)


## 🔹 Phase 1 — ✅ Completed  
**Build Your Home Cyber Lab**  
**Date:** November 4, 2025  

**Summary:**  
- Created two virtual machines (Windows 10 + Kali Linux) in VirtualBox.  
- Configured an **Internal Network** named `CyberLabNet`.  
- Verified connectivity with ICMP (ping) tests.  
- Captured traffic in Wireshark and saved evidence.

**Deliverables:**   
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

## 🧠 What This Shows (at a glance)

| Skill Area | Evidence |
|---|---|
| **Windows security auditing** | Exported **Event IDs 4625** (failed) and **4624** (successful) via PowerShell |
| **Python scripting** | `parser.py` summarizes top attacking IPs / targeted users + failed vs successful |
| **Network analysis** | **Wireshark** capture during logon attempts; timestamp correlation |
| **Lab design** | **VirtualBox**: Windows + Kali on an isolated network |
| **Reporting** | 1–2 page incident report template in `/report/` |

---

## 🧰 Stack

- **Virtualization:** VirtualBox (Windows 10/11 + Kali/Ubuntu)
- **OS/Tools:** Windows Event Viewer, PowerShell, Python 3, Wireshark
- **Learning:** TryHackMe (optional validation labs)

---
## 🏁 Project Timeline

| Phase | Description | Status | Date Completed | 
|-------|--------------|--------|--------------|
| 1 | Build Home Cyber Lab | 🟢 **Completed** | November 4, 2025 | 
| 2 | Collect Windows Event Logs | 🟢 **Completed** | November 5, 2025 |
| 3 | Python Log Parser | 🟢 **Completed** | November 6, 2025 |
| 4 | Network Correlation | ⚪ **Planned** |
| 5 | Documentation & Reporting | ⚪ **Planned** |
| 6 | Bonus: Dashboard + Automation | ⚪ **Planned** |