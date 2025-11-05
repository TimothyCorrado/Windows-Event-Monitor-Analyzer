# Windows Event Monitor & Analyzer (Home Cyber Lab)

[![Status](https://img.shields.io/badge/status-active-brightgreen)]()
[![Made with Python](https://img.shields.io/badge/Python-3.x-blue)]()
[![PowerShell](https://img.shields.io/badge/PowerShell-✓-blue)]()
[![Wireshark](https://img.shields.io/badge/Wireshark-✓-blue)]()
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Kali%20%7C%20VirtualBox-lightgrey)]()

![Status](https://img.shields.io/badge/Status-Phase%201%20Completed-brightgreen)
![Next](https://img.shields.io/badge/Next%20Up-Phase%202%20Planned-blue)
![Tools](https://img.shields.io/badge/Tools-VirtualBox%20%7C%20Kali%20%7C%20Wireshark-orange)
![Language](https://img.shields.io/badge/Language-PowerShell%20%7C%20Python-yellow)

Detect and summarize unusual Windows logon activity using **PowerShell + Python**, and correlate with **Wireshark** network captures — all inside a **VirtualBox** home lab (Windows + Kali).

> **Hiring managers:** This project simulates a junior SOC workflow: collect → parse → triage → correlate → report.

---

### 🗓️ Project Updates

## 🔹 Phase 1 — ✅ Completed
**Build Your Home Cyber Lab**  
**Date:** November 4, 2025  

**Summary:**  
- Created two virtual machines (Windows 10 + Kali Linux) in VirtualBox.  
- Configured an **Internal Network** named `CyberLabNet`.  
- Verified connectivity with ICMP (ping) tests.  
- Captured traffic in Wireshark and saved evidence.

**Deliverables:**  
- ![Lab Setup Screenshot](evidence/lab_setup.png)  
- [Wireshark Capture (lab_setup.pcapng)](evidence/lab_setup.pcapng)

---

## 🔹 Phase 2 — 🕓 Next Up
**Collect Windows Event Logs**

**Goal:**  
Export and analyze Windows Security Logs using PowerShell (`wevtutil`) for failed logon events (Event ID 4625).  
Prepare sample logs to feed into the Python parser in Phase 3.

**Planned Tasks:**  
- Enable and verify Windows event logging.  
- Simulate failed logons.  
- Export logs with PowerShell.  
- Transfer to Kali for analysis.

### 🧩 Phase 1: Build Your Home Cyber Lab

**Date:** November 3, 2025  
**Status:** In Progress ✅  

#### What I Set Up
- Installed **VirtualBox**
- Downloaded **Kali Linux ISO (installer)** and **Windows 10 ISO**
- Created two virtual machines:
  - Kali Linux (4GB RAM, 20GB Disk)
  - Windows 10 (4GB RAM, 40GB Disk)
- Configured both on an **Internal Network** (`CyberLabNet`)
- Began testing connectivity (Wireshark + ping)

#### Current Results
- Kali and Windows both installed successfully
- Wireshark running and ready to capture packets
- Encountered minor network communication issues (to fix next session)

#### Next Step
- Troubleshoot ping connectivity between VMs  
- Complete Wireshark packet capture for `lab_setup.png`  
- Proceed to **Phase 2: Collect Windows Logs**

---

## 🔎 Quick Preview

[![Click to view evidence](./evidence/lab_setup.png)](./evidence/wireshark_failedlogons.png)

*(Replace the two image files above with your screenshots: `evidence/lab_setup.png` and `evidence/wireshark_failedlogons.png`.)*

---

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

## 🚀 Run It

### 1) Export Windows Security logs (PowerShell as Admin)
```powershell
# Inside this repo folder (Windows VM)
.\scripts\export-logons.ps1
# Creates: .\logs\FailedLogons.txt and .\logs\SuccessfulLogons.txt

## 🏁 Project Timeline

| Phase | Description | Status |
|-------|--------------|--------|
| 1 | Build Home Cyber Lab | 🟢 **Completed** |
| 2 | Collect Windows Event Logs | ⚪ **Planned** |
| 3 | Python Log Parser | ⚪ **Planned** |
| 4 | Network Correlation | ⚪ **Planned** |
| 5 | Documentation & Reporting | ⚪ **Planned** |
| 6 | Bonus: Dashboard + Automation | ⚪ **Planned** |