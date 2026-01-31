import re
PHONE_REGEX = r"(\+?\d[\d\s\-\(\)]{8,}\d)"
EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"


def extract_emails(text):
    return set(re.findall(EMAIL_REGEX, text))

def extract_phones(text):
    raw_phones = re.findall(PHONE_REGEX, text)
    phones = set()
    for phone in raw_phones:
        cleaned = re.sub(r"[^\d+]", "", phone)
        phones.add(cleaned)
    return phones