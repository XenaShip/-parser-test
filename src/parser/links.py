from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def extract_links(html, base_url):
    if not html:
        return []
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for tag in soup.find_all("a", href=True):
        href = tag["href"].strip()
        if not href:
            continue
        if href.startswith("#"):
            continue
        if href.startswith(("mailto:", "tel:")):
            continue
        if href.startswith("javascript:"):
            continue
        if href.startswith("data:"):
            continue
        full_url = urljoin(base_url, href)
        parsed = urlparse(full_url)
        if parsed.scheme not in ("http", "https"):
            continue
        links.append(full_url)
    return links
