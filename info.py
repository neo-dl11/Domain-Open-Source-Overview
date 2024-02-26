from dnsrecord import get_dns_records
from phishing import check_phishing
from script import check_website_status  

def get_website_info(domain):
    website_url = "https://" + domain
    return check_website_status(website_url, domain), get_dns_records(domain), check_phishing(domain)

