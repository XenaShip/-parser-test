import sys
import json
from urllib.parse import urlparse
import logging
from .start_file import parse_site


def is_valid_url(url):
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def main():
    if len(sys.argv) >= 2:
        start_url = sys.argv[1].strip()
    else:
        start_url = input("URL: ").strip()

    if not start_url:
        print("error, incorrect URL")
        return

    if not is_valid_url(start_url):
        print("error, incorrect URL")
        print("exaple: https://github.com/XenaShip")
        return

    print("\nStart...\n")

    try:
        result = parse_site(start_url)
    except Exception as e:
        print("Exeption:", e)
        return

    print("Result:")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
