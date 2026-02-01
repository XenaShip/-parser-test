import re

EMAIL_REGEX = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"

PHONE_REGEX = r"(\+?\d[\d\s\-\(\)]{8,}\d)"

def extract_emails(text):
    if not text:
        return set()
    emails = set(re.findall(EMAIL_REGEX, text))
    emails.discard("you@domain.com")
    return emails


def extract_phones(text):
    if not text:
        return set()
    raw_matches = re.findall(PHONE_REGEX, text)
    phones = set()
    for phone in raw_matches:
        if phone.isdigit():
            continue
        if all(x not in phone for x in (" ", "-", "(", ")")):
            continue
        digits = re.sub(r"\D", "", phone)
        if not (10 <= len(digits) <= 15):
            continue
        if digits.startswith("8") and len(digits) == 11:
            digits = "7" + digits[1:]
        phones.add("+" + digits)
    return phones