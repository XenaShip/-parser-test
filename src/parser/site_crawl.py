from collections import deque
from urllib.parse import urlparse, urldefrag
import time

from .fetch_url import fetch_html
from .links import extract_links


def crawl(start_url, max_pages=10, delay=1):
    visited = set()
    queue = deque([start_url])
    domain = urlparse(start_url).netloc
    while queue and len(visited) < max_pages:
        url = queue.popleft()
        result = urldefrag(url)
        url = result[0]
        if url in visited:
            continue
        print("Обходим:", url)
        visited.add(url)
        html = fetch_html(url)
        if not html:
            continue
        time.sleep(delay)
        links = extract_links(html, url)
        for link in links:
            result = urldefrag(link)
            link = result[0]
            parsed_link = urlparse(link)
            if parsed_link.netloc != domain:
                continue
            if parsed_link.query:
                continue
            if link not in visited:
                queue.append(link)
    return visited
