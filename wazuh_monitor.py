import time
import json
import re

from virustotal import check_hash
from discord_alert import send_discord_alert
from n8n_sender import send_to_n8n


ALERT_FILE = "/var/ossec/logs/alerts/alerts.json"


def save_incident(result):
    with open("incidents.json", "a") as file:
        json.dump(result, file)
        file.write("\n")


def extract_sha256(alert):

    try:
        # FIM events
        if "syscheck" in alert:

            sha256 = alert["syscheck"].get("sha256_after")

            if sha256:
                return sha256

        # Fallback regex search
        data = json.dumps(alert)

        match = re.search(
            r"\b[a-fA-F0-9]{64}\b",
            data
        )

        if match:
            return match.group()

    except Exception as e:
        print("[!] Hash extraction error:", e)

    return None


def monitor():

    print("[+] Monitoring Wazuh alerts...")

    with open(ALERT_FILE, "r") as file:

        file.seek(0, 2)

        while True:

            line = file.readline()

            if not line:
                time.sleep(1)
                continue

            try:

                alert = json.loads(line)

                sha256 = extract_sha256(alert)

                if sha256:

                    print("\n" + "=" * 60)
                    print("[+] SHA256 Found:")
                    print(sha256)

                    print("\n[+] Querying VirusTotal...")

                    result = check_hash(sha256)


                    if result is None:

                        print("[+] File is clean. No alert sent.")


                    elif "error" in result:

                        print("[!] VirusTotal Error:")
                        print(result["error"])


                    else:

                        save_incident(result)

                        print("\nVirusTotal Scan Result")
                        print("=" * 60)

                        print(f"File Name   : {result.get('file_name')}")
                        print(f"SHA256      : {result.get('sha256')}")
                        print(f"Malicious   : {result.get('malicious')}")
                        print(f"Suspicious  : {result.get('suspicious')}")
                        print(f"Undetected  : {result.get('undetected')}")
                        print(f"Harmless    : {result.get('harmless')}")

                        # Send notifications
                        send_discord_alert(result)

                        send_to_n8n(result)


            except json.JSONDecodeError:

                print("[!] Invalid JSON alert skipped")


            except Exception as e:

                print("[!] Error:", e)



if __name__ == "__main__":

    monitor()
