# 🛡️ SOC Automation Lab: SIEM, Threat Intelligence & SOAR Pipeline

![SOC Automation](https://img.shields.io/badge/SOC-Automation-blue)
![Wazuh](https://img.shields.io/badge/SIEM-Wazuh-green)
![Python](https://img.shields.io/badge/Python-Automation-yellow)
![n8n](https://img.shields.io/badge/SOAR-n8n-orange)

## 📌 Project Overview

This project is a complete Security Operations Center (SOC) lab environment built to simulate real-world security monitoring, threat detection, malware analysis, and automated incident response.

The lab combines:

- SIEM monitoring using **Wazuh**
- Log analysis using **Splunk**
- Endpoint monitoring using **Sysmon**
- Malware analysis using **VirusTotal API**
- Automation and orchestration using **n8n**
- AI-powered incident reporting using **Grok AI Agent**
- Alert notification through **Discord**

The goal of this project was to build an automated security pipeline that can detect threats, analyze them, generate SOC reports, and notify analysts automatically.

---

# 🏗️ Architecture

                Malware Sample
                      |
                      |
              Python Malware Scanner
                      |
                      |
              VirusTotal API Analysis
                      |
                      |
                n8n SOAR Platform
                      |
          ----------------------------
          |                          |
    Severity Engine              AI Agent
          |                          |
          ----------------------------
                      |
                      |
              Discord SOC Alerts

Windows Endpoint
|
|
Wazuh Agent
|
|
Wazuh Manager
|
|
Wazuh Dashboard

Windows Logs
|
|
Sysmon + Splunk Forwarder
|
|
Splunk Enterprise


---

# 🔧 Technologies Used

## Security Tools

| Tool | Purpose |
|---|---|
| Wazuh | SIEM monitoring and security alerts |
| Splunk Enterprise | Log analysis |
| Sysmon | Endpoint telemetry collection |
| VirusTotal API | Threat intelligence |
| Nmap | Network scanning |
| Wireshark | Packet analysis |

## Development & Automation

| Tool | Purpose |
|---|---|
| Python | Security automation scripts |
| n8n | SOAR workflow automation |
| Grok AI | AI-based SOC reporting |
| Discord Webhook | Alert notification |

---

# 🚀 Implementation Steps

## 1. SOC Lab Environment Setup

Created a virtualized security environment using VirtualBox.

### Ubuntu VM

Used as:

- Wazuh Manager
- Wazuh Indexer
- Wazuh Dashboard
- Splunk Server

### Windows VM

Used as:

- Monitored endpoint
- Log generation machine
- Sysmon endpoint

---

# 2. Wazuh SIEM Deployment

Installed Wazuh using:

```bash
wazuh-install.sh -a

Configured:

Wazuh Manager
Wazuh Indexer
Wazuh Dashboard

Accessed dashboard for:

Security alerts
Agent management
Event monitoring
3. Endpoint Monitoring

Installed Wazuh Agent on Windows.

Configured communication between:

Windows Agent
        |
        |
Wazuh Manager

Collected:

System events
Security logs
File changes
Endpoint activity
4. File Integrity Monitoring (FIM)

Configured Wazuh FIM to monitor:

C:\Users\Public

Detected:

File creation
File modification
File deletion
5. Splunk Integration

Installed:

Splunk Enterprise
Splunk Universal Forwarder

Configured log forwarding:

Windows Logs
      |
      |
Splunk Universal Forwarder
      |
      |
Splunk Enterprise

Collected:

Windows Event Logs
Sysmon Events
6. Sysmon Deployment

Installed Sysmon for advanced endpoint visibility.

Monitored:

Process creation
Network connections
Registry activity
File operations
7. Malware Analysis Automation

Created Python malware analysis automation.

Workflow:

Malware File
      |
      |
SHA256 Hash Generation
      |
      |
VirusTotal API
      |
      |
Threat Intelligence Result

Extracted:

File name
SHA256 hash
Malicious detections
Suspicious detections
Undetected results
8. n8n SOAR Automation

Created an automated security workflow.

Workflow:

Python Scanner
       |
       |
n8n Webhook
       |
       |
Severity Calculation
       |
       |
IF Condition
       |
       |
AI Agent
       |
       |
Discord Alert
9. Automated Severity Classification

Implemented severity logic:

Malicious >= 20
        |
     CRITICAL


Malicious 5-19
        |
       HIGH


Malicious 1-4
        |
      MEDIUM


Malicious 0
        |
       LOW
10. AI SOC Analyst Integration

Integrated Grok AI Agent.

The AI receives:

Malware information
Detection statistics
Severity level

Generates:

Threat summary
Detection analysis
Risk assessment
Recommended actions
11. Discord Alert Automation

Final alerts are automatically delivered to Discord.

Example alert:

🚨 Security Alert

Severity: HIGH

File:
malware.exe

SHA256:
xxxxxxxx

VirusTotal Detection:
Malicious: 26

Recommended Actions:
- Isolate endpoint
- Block hash
- Investigate activity
🧪 Testing

The system was tested using malware samples.

Successful execution:

✅ Malware detected
✅ VirusTotal analysis completed
✅ Severity calculated
✅ AI report generated
✅ Discord alert received

📂 Repository Structure
SOC-Automation-Lab/

│
├── python/
│   ├── malware_scanner.py
│   ├── virustotal.py
│
├── n8n/
│   └── workflow.json
│
├── wazuh/
│   └── configurations/
│
├── splunk/
│   └── configurations/
│
├── screenshots/
│
└── README.md
🎯 Skills Demonstrated
Cybersecurity
SOC Operations
SIEM Deployment
Threat Intelligence
Malware Analysis
Incident Response
Automation
SOAR Workflows
API Integration
Webhooks
Security Automation
Programming
Python scripting
JSON handling
API communication
AI Security
LLM integration
Automated security reporting
AI-assisted investigation
