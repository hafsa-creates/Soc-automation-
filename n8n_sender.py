import requests

# Replace with YOUR webhook URL

WEBHOOK_URL = ""
def send_to_n8n(data):
    try:
        response = requests.post(
            WEBHOOK_URL,
            json=data,
            timeout=10
        )
        print(f"[+] Sent to n8n (HTTP {response.status_code})")
    except Exception as e:
        print(f"[!] Failed to send to n8n: {e}")
