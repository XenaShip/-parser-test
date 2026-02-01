import re


EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
PHONE_REGEX = r"(\+?\d[\d\s\-\(\)]{9,}\d)"


def extract_emails(text):
    if not text:
        return set()
    emails = set(re.findall(EMAIL_REGEX, text))
    emails.discard("you@domain.com")
    return emails



def extract_phones(text):
    if not text:
        return set()
    raw_phones = re.findall(PHONE_REGEX, text)
    phones = set()
    for phone in raw_phones:
        if "-" not in phone and " " not in phone and "(" not in phone:
            continue
        cleaned = re.sub(r"[^\d+]", "", phone)
        digits = re.sub(r"\D", "", cleaned)
        if len(digits) < 10 or len(digits) > 15:
            continue
        if cleaned.startswith("+"):
            phones.add(cleaned)
        elif digits.startswith("7") or digits.startswith("8"):
            if len(digits) == 11:
                phones.add(digits)
    return phones



