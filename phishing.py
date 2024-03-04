import requests

def check_google_safe_browsing(domain, api_key):
    url = "https://safebrowsing.googleapis.com/v4/threatMatches:find"
    payload = {
        "client": {
            "clientVersion": "1.0.0"
        },
        "threatInfo": {
            "threatTypes": ["SOCIAL_ENGINEERING", "MALWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [
                {"url": f"http://{domain}/"},
                {"url": f"https://{domain}/"}
            ]
        }
    }

    headers = {'Content-Type': 'application/json'}
    params = {'key': api_key}

    response = requests.post(url, headers=headers, params=params, json=payload)
    reported = (f"⚠️T the domain '{domain}' is on the google phishing list.")
    not_reported = (f"✅  The domain '{domain}' is not on the google phishing list.")

    if response.ok:
        data = response.json()
        if 'matches' in data:
            return reported  
        else:
            return not_reported
    else:
        print(f"Error checking phishing status: {response.status_code}")
        return None  
