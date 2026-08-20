# 🤖 Threat Intelligence API Integrator

An automated Python-based Security Operations tool that queries the **AbuseIPDB API** to evaluate IP address reputation, parse JSON telemetry, and format actionable threat metrics.

## 🛠️ Features & Security Controls
* 🔒 **Secure Credential Storage:** Uses `python-dotenv` and `.gitignore` to prevent API key leaks in public repositories.
* 🛡️ **Input Validation:** Employs Python's `ipaddress` module to validate IPv4/IPv6 formats before issuing HTTP requests.
* 📊 **Telemetry Parsing:** Extracts abuse confidence scores, ISP info, total reports, domain details, and Tor node status.

## 🚀 Quickstart Guide
1. **Clone repository & enter directory:**
   ```bash
   git clone https://github.com/ryguitarguy/threat-intel-integrator
   cd threat-intel-integrator
