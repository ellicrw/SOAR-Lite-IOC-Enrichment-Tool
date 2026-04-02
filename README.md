# SOAR Lite IOC Enrichment Tool

## Overview

This project simulates a lightweight SOAR (Security Orchestration, Automation, and Response) workflow by automating IOC (Indicator of Compromise) enrichment using the VirusTotal API.

The tool is designed to replicate Tier 1 SOC analyst tasks such as:

* Querying threat intelligence platforms
* Enriching file hash indicators
* Producing structured JSON output for further analysis

---

## Features

* VirusTotal API integration for file hash lookups
* JSON-formatted enrichment output
* CLI-based workflow for automation pipelines
* Error handling for failed API requests
* Environment variable support for secure API key management

---

## Tech Stack

* Python 3
* Requests
* python-dotenv

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/soar-lite-ioc-enrichment.git
cd soar-lite-ioc-enrichment
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Rename `.env.example` to `.env` and add your API key:

```
VT_API_KEY=your_actual_api_key
```

---

## Usage

```bash
python src/vt_enrichment.py <file_hash>
```

### Example:

```bash
python src/vt_enrichment.py 44d88612fea8a8f36de82e1278abb02f
```

---

## Sample Output

```json
{
    "source": "virustotal",
    "hash": "44d88612fea8a8f36de82e1278abb02f",
    "malicious": 12,
    "suspicious": 2,
    "undetected": 45,
    "harmless": 5
}
```

---

## Use Case (SOC Simulation)

This tool demonstrates how security analysts automate repetitive enrichment tasks during alert triage. It can be extended into a full pipeline by:

* Adding AbuseIPDB integration
* Supporting IP/domain indicators
* Feeding results into SIEM dashboards
* Automating alert tagging

---

## Future Improvements

* Multi-IOC support (IP, domain, URL)
* Parallel API requests for batch processing
* Integration with AbuseIPDB
* Logging and alert scoring system
* Output export to CSV or SIEM-compatible formats

---

## Resume Bullet Points

* Developed a Python-based SOAR-lite tool to enrich IOC indicators using VirusTotal API
* Automated threat intelligence lookups and reduced manual triage effort
* Generated structured JSON outputs for downstream security analysis workflows

---

## Disclaimer

This project is for educational purposes only. Ensure compliance with API usage policies when integrating into production systems.
