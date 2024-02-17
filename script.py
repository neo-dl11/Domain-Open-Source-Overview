import requests
import whois
import ssl
from OpenSSL import crypto
from datetime import datetime, date
import json

class WhoisInfo:
    def __init__(self, domain_name, creation_date, expiration_date, registrar):
        self.domain_name = domain_name
        self.creation_date = creation_date
        self.expiration_date = expiration_date
        self.registrar = registrar

    def to_dict(self):
        return {
            "Domain Name": self.domain_name,
            "Creation Date": self.creation_date,
            "Expiration Date": self.expiration_date,
            "Registrar": self.registrar
        }

class SSLInfo:
    def __init__(self, subject, issuer, valid_from, valid_until):
        self.subject = subject
        self.issuer = issuer
        self.valid_from = valid_from
        self.valid_until = valid_until

    def to_dict(self):
        return {
            "Subject": self.subject,
            "Issuer": self.issuer,
            "Valid From": self.valid_from,
            "Valid Until": self.valid_until
        }

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)

def get_whois_info(domain_name, fields=None):
    try:
        whois_info = whois.whois(domain_name)
        
        if fields:
            return {field.capitalize(): whois_info.get(field, 'N/A') for field in fields}
        else:
            return whois_info
    except whois.parser.PywhoisError as e:
        print(f"Error fetching WHOIS information: {e}")
        return {}  

def check_website_status(url, domain):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        print(f"Website is up! Status code: {response.status_code}")

        whois_info = get_whois_info(url)
        
        if whois_info:
            whois_obj = WhoisInfo(
                whois_info.get("domain_name", "N/A"),
                whois_info.get("creation_date", "N/A"),
                whois_info.get("expiration_date", "N/A"),
                whois_info.get("registrar", "N/A")
            )
        else:
            whois_obj = WhoisInfo("N/A", "N/A", "N/A", "N/A")

        # SSL Certificate Information
        try:
            cert = ssl.get_server_certificate((domain, 443))
            x509 = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
            not_before = x509.get_notBefore().decode('utf-8')
            not_after = x509.get_notAfter().decode('utf-8')
            ssl_obj = SSLInfo(
                format_x509_component(x509.get_subject().get_components()),
                format_x509_component(x509.get_issuer().get_components()),
                datetime.strptime(not_before, '%Y%m%d%H%M%SZ').strftime('%Y-%m-%d %H:%M:%S'),
                datetime.strptime(not_after, '%Y%m%d%H%M%SZ').strftime('%Y-%m-%d %H:%M:%S')
            )
        except Exception as e:
            print(f"Error fetching SSL certificate: {e}")
            ssl_obj = SSLInfo("N/A", "N/A", "N/A", "N/A")

        result_dict = {
            "Website Status": "Up",
            "WHOIS Information": whois_obj.to_dict(),
            "SSL Certificate Information": ssl_obj.to_dict()
        }
        return result_dict
    except requests.exceptions.RequestException as e:
        print(f"Error checking website status: {e}")
        return json.dumps({"error": "Website is down or cannot be reached."})  # Return an error message

def format_x509_component(components):
    return ", ".join(f"{key.decode('utf-8')}={value.decode('utf-8')}" for key, value in components)
