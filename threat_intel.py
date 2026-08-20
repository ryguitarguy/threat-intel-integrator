import os
import requests
import ipaddress
from dotenv import load_dotenv

# 1. Load API key securely 🔒
load_dotenv()
API_KEY = os.getenv("ABUSEIPDB_API_KEY")

if not API_KEY:
    print("❌ Error: ABUSEIPDB_API_KEY not found in .env file.")
    exit(1)

# 2. Accept dynamic input from user 🎯
target_ip = input("Enter an IP address to analyze: ").strip()

# 3. Validate IP address format 🛡️
try:
    ipaddress.ip_address(target_ip)
except ValueError:
    print(f"❌ Error: '{target_ip}' is not a valid IPv4 or IPv6 address.")
    exit(1)

url = "https://api.abuseipdb.com/api/v2/check"
headers = {
    "Accept": "application/json",
    "Key": API_KEY
}
params = {
    "ipAddress": target_ip,
    "maxAgeInDays": "90"
}

# 4. Issue GET request 🌐
try:
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json().get("data", {})
        
        print("\n" + "=" * 45)
        print(f"📊 THREAT INTELLIGENCE REPORT: {data.get('ipAddress')}")
        print("=" * 45)
        print(f"  • Abuse Confidence Score : {data.get('abuseConfidenceScore')}%")
        print(f"  • ISP                    : {data.get('isp')}")
        print(f"  • Domain                 : {data.get('domain')}")
        print(f"  • Country Code           : {data.get('countryCode')}")
        print(f"  • Usage Type             : {data.get('usageType')}")
        print(f"  • Total Reports (90 days): {data.get('totalReports')}")
        print(f"  • Tor Exit Node          : {data.get('isTor')}")
        print("=" * 45 + "\n")
    else:
        print(f"\n❌ Request failed [Status {respose.status_code}]: {response.text}")

except Exception as e:
    print(f"\n❌ Network or connection error: {e}")
