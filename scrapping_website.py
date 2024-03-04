import requests
from bs4 import BeautifulSoup

def scrape_website(domain):
    try:
        url = f"http://www.{domain}"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else "No title found"
            meta_keywords = soup.find("meta", attrs={"name": "keywords"})
            keywords = meta_keywords["content"] if meta_keywords else "No meta keywords found"
            meta_description = soup.find("meta", attrs={"name": "description"})
            description = meta_description["content"] if meta_description else "No meta description found"
            
            return {
                "title": title,
                "keywords": keywords,
                "description": description
            }
        else:
            print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error scraping website: {e}")
        return None
