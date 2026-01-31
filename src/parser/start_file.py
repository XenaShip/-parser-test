from .fetch_url import fetch_html

def parse_site(start_url):
    return {
        "url": start_url,
        "emails": [],
        "phones": [],
    }

html1 = fetch_html("https://hh.ru/vacancy/129638161?hhtmFrom=chat")

if html1:
    print("скачено")
    print(html1[:500])
else:
    print("не удалось загрузить страницу")


html2 = fetch_html("https://example.com")

if html2:
    print("скачено")
    print(html2[:500])
else:
    print("не удалось загрузить страницу")
