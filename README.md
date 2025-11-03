# Windows Event Monitor & Analyzer (Home Cyber Lab)

[![Status](https://img.shields.io/badge/status-active-brightgreen)]()
[![Made with Python](https://img.shields.io/badge/Python-3.x-blue)]()
[![PowerShell](https://img.shields.io/badge/PowerShell-✓-blue)]()
[![Wireshark](https://img.shields.io/badge/Wireshark-✓-blue)]()
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Kali%20%7C%20VirtualBox-lightgrey)]()

Detect and summarize unusual Windows logon activity using **PowerShell + Python**, and correlate with **Wireshark** network captures — all inside a **VirtualBox** home lab (Windows + Kali).

> **Hiring managers:** This project simulates a junior SOC workflow: collect → parse → triage → correlate → report.

---

### 🗓️ Project Updates
> **Update (Nov 2, 2025):** Completed first successful parser run — analyzed Event IDs **4625** and **4624**, verified triage output and generated `triage.txt`.

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

> Security+ mapping is in `Security+_Objectives_Mapped.txt` (kept separate to avoid clutter).

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
