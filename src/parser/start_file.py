from .site_crawl import crawl


def parse_site(start_url):
    emails, phones = crawl(start_url, max_pages=5, delay=0)
    return {
        "url": start_url,
        "emails": sorted(emails),
        "phones": sorted(phones),
    }