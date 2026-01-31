from .fetch_url import fetch_html
from .links import extract_links
from .site_crawl import crawl
from .contacts import extract_emails, extract_phones

def parse_site(start_url):
    return {
        "url": start_url,
        "emails": [],
        "phones": [],
    }

text = """
Contact us:
email: test@gmail.com
phone: +7 (999) 123-45-67
phone: 8 495 111 22 33
"""

print(extract_emails(text))
print(extract_phones(text))