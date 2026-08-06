# SOC Automation Lab

**Building a SIEM-to-SOAR Detection & Response Pipeline**

Wazuh · Sysmon · VirusTotal · Python · n8n · Groq AI · Discord

A home-lab Security Operations Center pipeline that takes a detection from raw
endpoint telemetry through automated enrichment, AI-assisted triage, and
analyst notification — with no manual steps in between.

---

## Overview

A monitored Windows endpoint generates activity (new processes, file changes,
network events). Wazuh, running on an Ubuntu server, collects and analyzes
that telemetry via its agent and Sysmon integration. A custom Python monitor
watches Wazuh's alert stream, extracts file hashes, and submits them to the
VirusTotal API. The enriched result is forwarded to an n8n workflow, which
calculates a severity score, branches on that score, asks a Groq-hosted LLM
to draft a human-readable threat report, and posts the complete alert —
verdict, evidence, and recommended response — to a dedicated Discord channel.

Two notification paths exist by design: the Python script posts a fast,
minimal Discord alert the moment a verdict is available, while the n8n
workflow independently produces a richer, AI-narrated incident report on the
same data — giving both immediacy and depth.

## Architecture

**Detection & Enrichment Chain**

```
Windows Endpoint → Wazuh Agent → Wazuh SIEM (Manager / Indexer / Dashboard)
Windows Event Logs + Sysmon → Wazuh Agent → Wazuh SIEM
Wazuh Alert → wazuh_monitor.py → SHA256 Hash → VirusTotal API → Verdict
```

**Orchestration & Response Chain**

```
VirusTotal Verdict → n8n Webhook → calculate severity → IF (branch)
→ AI Agent (Groq LLM) → Formatted Threat Report → Discord #alerts
```

## Components

| Component | Role |
|---|---|
| **Wazuh** | Core SIEM — Manager, Indexer, Dashboard. Agent-based collection, built-in File Integrity Monitoring, REST-friendly alert log. |
| **Sysmon** | Extends Windows telemetry beyond default event logs — process creation with full command lines, network connections, file activity, registry changes. |
| **wazuh_monitor.py** | Tails the Wazuh alert log in real time, detects new-process events, computes SHA256 hashes, and queries VirusTotal for a verdict. |
| **hash_parser.py** | Helper that extracts a file's SHA256 hash from a Wazuh alert for downstream lookup. |
| **discord_notifier.py** | Posts a fast, minimal Discord alert the moment a verdict is available. |
| **incidents.json / incident_report.txt** | Structured and human-readable logs of every analyzed file — timestamp, filename, hash, VirusTotal counts, derived severity. |
| **n8n** | No-code SOAR engine — webhook trigger, severity calculation, conditional branching, AI Agent orchestration. |
| **Groq (llama-3.3-70b-versatile)** | Drafts the analyst-facing incident narrative: threat summary, detection details, threat assessment, recommended SOC actions. |
| **Discord** | Real-time alerting surface — a dedicated `#alerts` channel receives both the fast Python alert and the rich AI-narrated report. |

## Lab Environment

- **Ubuntu 24.04 LTS** — hosts Wazuh Manager/Indexer/Dashboard, the Python automation scripts, and n8n.
- **Windows 10 endpoint** — the monitored client, fitted with the Wazuh agent and Sysmon.
- Both VMs run under VirtualBox on a shared **NAT Network**, so the endpoint and SOC host can reach each other on a private subnet.

## Build Highlights

1. Deployed Wazuh (Manager, Indexer, Dashboard) via the official all-in-one installer.
2. Enrolled the Windows endpoint as an agent, resolving an initial VirtualBox NAT vs. NAT Network mismatch.
3. Installed Sysmon and extended the agent's `ossec.conf` to ingest the Sysmon event channel — validated with a Discover query (58 matching events) and a separate FIM check (43 syscheck hits).
4. Built `wazuh_monitor.py` to tail alerts, hash new processes, and query VirusTotal, persisting every result to `incidents.json`.
5. Added Discord alerting so detections reach an analyst without watching a terminal.
6. Stood up n8n as the SOAR engine: a webhook trigger, an IF node for severity branching, and an AI Agent wired to a Groq Chat Model.
7. Diagnosed and fixed an intermittent webhook `HTTP 404` — the workflow wasn't published/listening — and added a dedicated "calculate severity" node so severity is derived consistently inside the workflow.
8. Verified a complete end-to-end run: VirusTotal verdict → Discord alert → n8n webhook (`HTTP 200`) → AI-authored report posted to `#alerts`.

## Skills Demonstrated

- SIEM deployment and administration (Wazuh: Manager, Indexer, Dashboard, agent enrollment)
- Endpoint telemetry engineering (Sysmon configuration, File Integrity Monitoring)
- Security automation scripting in Python (log tailing, hashing, REST API integration with VirusTotal)
- SOAR workflow design in n8n (webhooks, conditional branching, AI Agent / LLM integration via Groq)
- Real-time alerting integration (Discord webhook notifications)
- Systematic troubleshooting of a multi-system pipeline (VM networking, agent enrollment, webhook failures)

## Repository Structure

```
soc-automation-lab/
├── wazuh_monitor.py        # Core detection + enrichment loop
├── hash_parser.py          # SHA256 extraction helper
├── discord_notifier.py     # Fast Discord alert module
├── test_vt.py               # VirusTotal API connectivity check
├── test_discord.py          # Discord webhook connectivity check
├── test_n8n.py               # n8n webhook connectivity check
├── incidents.json           # Structured incident log (generated)
├── incident_report.txt      # Human-readable incident summary (generated)
├── n8n-workflow.json        # Exported SOAR workflow (Webhook → severity → IF → AI Agent → Discord)
└── README.md
```

> Adjust the tree above to match your actual repo layout before publishing.

## Disclaimer

This is a home-lab / educational project. Credentials, API keys, and internal
IP addresses shown in the accompanying report and screenshots are not
reproduced here and should never be committed to source control — use
environment variables or a secrets manager for `VIRUSTOTAL_API_KEY`,
`DISCORD_WEBHOOK_URL`, and your Groq API key.

## Full Documentation

The complete build report — with step-by-step screenshots of every stage —
is included in this repository. See the presentation slides for a visual
walkthrough of the pipeline.

---

*Built as a personal SOC automation lab exercise, integrating open-source
security tooling with custom scripting and no-code orchestration.*
