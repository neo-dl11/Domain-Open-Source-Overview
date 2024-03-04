from dnsrecord import get_dns_records
from phishing import check_google_safe_browsing
from scrapping_website import scrape_website
from social_media import search_reddit_for_domain
from website_status import check_website_status

def get_website_info(domain):
    website_url = "https://" + domain
    return check_website_status(website_url, domain), get_dns_records(domain), check_google_safe_browsing(domain, 'API_KEY'), scrape_website(domain) 

def normalize_domain(domain):
    domains = domain.split(', ')
    normalized_domains = [d.lower() for d in domains]
    return normalized_domains[0]

def get_socialmedia_infos(domain):
    return search_reddit_for_domain(domain)
