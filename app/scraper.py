import requests
from bs4 import BeautifulSoup
import pprint
from urllib.parse import urljoin

def find_all_links(base_url):
    response = requests.get(base_url, timeout=5)
    soup = BeautifulSoup(response.text, "html.parser")

    links = set()
    for a in soup.find_all("a", href=True):
        href = a["href"]
        absolute_url = urljoin(base_url, href) 
        if absolute_url.startswith(base_url):  
            links.add(absolute_url)

    return list(links)


all_links = find_all_links('https://calorizator.ru')
pprint.pprint(all_links)


