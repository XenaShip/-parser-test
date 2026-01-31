from bs4 import BeautifulSoup
from urllib.parse import urljoin


def extract_links(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for tag in soup.find_all("a"):
        href = tag.get("href")
        if not href:
            continue
        if href.startswith("#"):
            continue
        if href.startswith("mailto:"):
            continue
        if href.startswith("tel:"):
            continue
        full_url = urljoin(base_url, href)
        links.append(full_url)

    return links
