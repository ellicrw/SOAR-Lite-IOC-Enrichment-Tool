import requests
import os

API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual VirusTotal API key

BASE_URL = "https://www.virustotal.com/api/v3"

file_hash = "YOUR_FILE_HASH_HERE"  # Replace with the actual file hash you want to query

def get_file_report(file_hash):
    url = f"{BASE_URL}/files/{file_hash}"
    headers = {"x-apikey": API_KEY}

    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        return {"source": "virustotal", "error": r.text}

    data = r.json()

    attrs = data.get("data", {}).get("attributes", {})

    stats = attrs.get("last_analysis_stats")

    if not stats:
        return {
            "source": "virustotal",
            "hash": file_hash,
            "status": "no_analysis_data",
            "raw": data
        }

    return {
        "source": "virustotal",
        "hash": file_hash,
        "malicious": stats.get("malicious", 0),
        "suspicious": stats.get("suspicious", 0),
        "undetected": stats.get("undetected", 0),
        "harmless": stats.get("harmless", 0),
    }
    
    

    
print(get_file_report(file_hash))
