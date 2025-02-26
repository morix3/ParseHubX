import requests
from bs4 import BeautifulSoup

def parse_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    site_title = soup.title.string if soup.title else "Без заголовка"
    meta_tags = {tag.get('name'): tag.get('content') for tag in soup.find_all('meta')}

    return {
        'title': site_title,
        'meta_tags': meta_tags
    }
