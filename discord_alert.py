
import requests

WEBHOOK_URL = ""


def send_discord_alert(result):
    message = f"""
🚨 **Malware Detected!**

**File:** {result['file_name']}
**SHA256:** `{result['sha256']}`

⚠️ Malicious: {result['malicious']}
🟡 Suspicious: {result['suspicious']}
"""

    response = requests.post(
        WEBHOOK_URL,
        json={"content": message}
    )

    if response.status_code == 204:
        print("[+] Discord alert sent!")
    else:
        print(f"[!] Discord Error: {response.status_code}")
