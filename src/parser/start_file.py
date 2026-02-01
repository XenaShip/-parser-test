from .fetch_html import fetch_html
from .links import extract_links
from .site_crawl import crawl
from .contacts import extract_emails, extract_phones

def parse_site(start_url):
    emails, phones = crawl(start_url, max_pages=5, delay=0)
    return {
        "url": start_url,
        "emails": sorted(emails),
        "phones": sorted(phones),
    }