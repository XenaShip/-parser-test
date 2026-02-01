from parser.contacts import extract_emails, extract_phones


def test_email_ok():
    text = "xena@ship.test"
    emails = extract_emails(text)
    assert "xena@ship.test" in emails


def test_email_ignore_js():
    text = "ship@3.5.7"
    emails = extract_emails(text)
    assert len(emails) == 0


def test_email_mix():
    text = "ship@3.5.7 xena@ship.test"
    emails = extract_emails(text)
    assert "xena@ship.test" in emails
    assert "ship@3.5.7" not in emails


def test_phone_ok():
    text = "+7 (200) 300-03-03"
    phones = extract_phones(text)
    assert "+72003000303" in phones


def test_phone_ignore_big_number():
    text = "20032003200320032003"
    phones = extract_phones(text)
    assert len(phones) == 0


def test_phone_empty():
    phones = extract_phones("")
    assert phones == set()

def test_phone_ignore_digits():
    text = "1704837122"
    phones = extract_phones(text)
    assert len(phones) == 0
