import requests

API_KEY = ""


def check_hash(file_hash):

    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"

    headers = {
        "x-apikey": API_KEY
    }

    print(f"[*] URL: {url}")
    print("[*] Sending request to VirusTotal...")

    response = requests.get(url, headers=headers)

    print("[*] Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()

        stats = data["data"]["attributes"]["last_analysis_stats"]

        result = {
            "file_name": data["data"]["attributes"].get("meaningful_name"),
            "sha256": data["data"]["attributes"].get("sha256"),
            "malicious": stats.get("malicious", 0),
            "suspicious": stats.get("suspicious", 0),
            "undetected": stats.get("undetected", 0),
            "harmless": stats.get("harmless", 0)
        }

        # Only return malicious or suspicious files
        if result["malicious"] > 0 or result["suspicious"] > 0:
            return result
        else:
            return None

    elif response.status_code == 404:
        return {
            "error": "Hash not found in VirusTotal"
        }

    elif response.status_code == 401:
        return {
            "error": "Invalid VirusTotal API Key"
        }

    else:
        return {
            "error": f"VirusTotal API Error: {response.status_code}"
        }
