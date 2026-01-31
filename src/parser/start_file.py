from .fetch_url import fetch_html
from .links import extract_links

def parse_site(start_url):
    return {
        "url": start_url,
        "emails": [],
        "phones": [],
    }


start_url = "https://example.com"

html = fetch_html(start_url)

if not html:
    print("Не удалось загрузить страницу")
    exit()

links = extract_links(html, start_url)

print("Найденные ссылки:")
for link in links:
    print(link)
