from parser.contacts import extract_emails, extract_phones


def test_extract_emails_basic():
    text = "Contact: xenaship@gmail.com and shipxena2003@site.ru"
    emails = extract_emails(text)

    assert "xenaship@gmail.com" in emails
    assert "shipxena2003@site.ru" in emails


def test_extract_emails_removes_placeholder():
    text = "Example email: you@domain.com"
    emails = extract_emails(text)

    assert "you@domain.com" not in emails


def test_extract_phones_valid():
    text = "Call Xena Ship: +7 (999) 123-45-67"
    phones = extract_phones(text)

    assert "+79991234567" in phones


def test_extract_phones_ignores_ids():
    text = "XenaShip internal id: 838860816777213 should not be a phone"
    phones = extract_phones(text)

    assert len(phones) == 0
