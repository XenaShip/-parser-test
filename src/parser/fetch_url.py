import requests


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "ru,en;q=0.9",
}

def fetch_html(url):
    try:
        response = requests.get(
            url,
            timeout=10,
            headers=HEADERS,
        )
        response.raise_for_status()

        return response.text

    except requests.RequestException as e:
        print(f"Ошибка при загрузке {url}: {e}")
        return None
