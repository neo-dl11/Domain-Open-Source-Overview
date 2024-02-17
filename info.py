from script import check_website_status  

def get_website_info(domain):
    website_url = "https://" + domain
    return check_website_status(website_url, domain)
