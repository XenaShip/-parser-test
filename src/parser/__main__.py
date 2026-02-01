import sys
import json
from urllib.parse import urlparse

from .start_file import parse_site


def is_valid_url(url):
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)


def main():
    if len(sys.argv) >= 2:
        start_url = sys.argv[1].strip()
    else:
        start_url = input("Введите стартовый URL сайта: ").strip()

    if not start_url:
        print("Ошибка: URL не введён")
        return

    if not is_valid_url(start_url):
        print("Ошибка: введён некорректный URL")
        print("Пример правильного ввода: https://github.com/XenaShip")
        return

    print("\nПарсер запущен...\n")

    try:
        result = parse_site(start_url)
    except Exception as e:
        print("Неожиданная ошибка во время работы парсера:", e)
        return

    print("✅ Результат:")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
