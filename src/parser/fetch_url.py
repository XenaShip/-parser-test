import requests


def fetch_html(url):
    try:
        response = requests.get(
            url,
            timeout=5,
            headers={"User-Agent": "Mozilla/5.0"},
            allow_redirects=True
        )
        response.raise_for_status()
        return response.text

    except requests.RequestException as e:
        print(f"Ошибка при загрузке {url}: {e}")
        return None
