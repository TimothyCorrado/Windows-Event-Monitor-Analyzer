# Incident Report — Windows Logon Anomaly

**Author:** Timothy Corrado  
**Date (UTC):** <YYYY-MM-DD>  
**Environment:** VirtualBox (Windows + Kali)  

## 1. Executive Summary
Briefly describe what occurred (e.g., surge in failed logons aligned with RDP attempts).

## 2. Timeline
- <HH:MM> — Began Wireshark capture
- <HH:MM> — Generated test failed logons on Windows
- <HH:MM> — Parser summary produced
- <HH:MM> — Findings documented

## 3. Indicators of Compromise (IOCs)
- Event IDs: 4625 (failed), 4624 (successful)
- Source IPs: <list>
- Target accounts: <list>
- Ports/Protocols observed: RDP(3389), SMB(445), ICMP

## 4. Analysis & Findings
- Volume of failed logons
- Top source IPs and targeted accounts
- Correlation with network captures

## 5. Containment, Eradication, Recovery (if applicable)
- Account lockout / password reset
- Restrict RDP (disable/public denylist/VPN)
- Monitoring/alerting recommendations

## 6. Recommendations
- Enforce MFA where possible
- Implement account lockout policy
- SIEM alert for repeated 4625 from same IP
- Ongoing log reviews and dashboard
