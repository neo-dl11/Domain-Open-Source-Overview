from flask import json
import requests

def check_google_safe_browsing(url):
    api_key = ""
    url = "https://safebrowsing.googleapis.com/v4/threatMatches:find"
    payload = {
        "threatInfo": {
            "threatTypes": ["SOCIAL_ENGINEERING", "MALWARE", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }
    response = requests.post(url, params={"key": api_key}, json=payload)
    if response.ok:
        data = response.json()
        if data.get("matches"):
            return {"phishing": True, "source": "Google Safe Browsing"}
    return {"phishing": False}

def check_urlscan(url):
    api_key = ""
    url = f"https://urlscan.io/api/v1/scan/"
    payload = {"url": url}
    headers = {"API-Key": api_key}
    response = requests.post(url, json=payload, headers=headers)
    if response.ok:
        data = response.json()
        if data.get("verdicts", {}).get("overall", "") == "malicious":
            return {"phishing": True, "source": "URLScan", "details": data}
    return {"phishing": False}

def check_phishing(url):
    sources = []
    details = {}
    phishing_detected = False
    
    result = check_google_safe_browsing(url)
    if result["phishing"]:
        phishing_detected = True
        sources.append(result["source"])
    
    result = check_urlscan(url)
    if result["phishing"]:
        phishing_detected = True
        sources.append(result["source"])
        details[result["source"]] = result["details"]
    
    return {"phishing_detected": phishing_detected, "sources": sources, "details": details}

url = ""
result = check_phishing(url)
if result["phishing_detected"]:
    print("Phishing detected!")
    print("Detected by sources:", result["sources"])
    print(result["details"])
else:
    print("No phishing detected.")
