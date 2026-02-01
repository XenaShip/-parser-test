from collections import deque
from urllib.parse import urlparse, urldefrag
import time
import logging

from .fetch_html import fetch_html
from .links import extract_links
from .contacts import extract_emails, extract_phones

logger = logging.getLogger(__name__)


def crawl(start_url, max_pages=30, delay=0.5):
    visited = set()
    queue = deque([start_url])
    emails = set()
    phones = set()
    domain = urlparse(start_url).netloc
    logger.info("Start crawling: %s", start_url)
    while queue and len(visited) < max_pages:
        url = queue.popleft()
        url = urldefrag(url)[0]
        if url in visited:
            continue
        visited.add(url)
        logger.info("Visiting (%d/%d): %s", len(visited), max_pages, url)
        html = fetch_html(url)
        if not html:
            logger.warning("No HTML fetched: %s", url)
            continue
        emails.update(extract_emails(html))
        phones.update(extract_phones(html))
        try:
            links = extract_links(html, url)
        except Exception as e:
            logger.warning("Link extraction failed on %s: %s", url, e)
            continue
        for link in links:
            link = urldefrag(link)[0]
            parsed = urlparse(link)
            if parsed.netloc != domain:
                continue
            link = parsed._replace(query="").geturl()
            if link not in visited:
                queue.append(link)
        time.sleep(delay)
    logger.info(
        "Crawling finished. Found %d emails, %d phones",
        len(emails), len(phones)
    )
    return emails, phones
