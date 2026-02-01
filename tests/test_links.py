from parser.links import extract_links


def test_extract_links_relative_to_absolute():
    html = '<a href="/xena-contacts">Contacts</a>'
    links = extract_links(html, "https://xenaship.com")

    assert "https://xenaship.com/xena-contacts" in links


def test_extract_links_skips_mailto_and_anchor():
    html = """
    <a href="#team">Team</a>
    <a href="mailto:xenaship@gmail.com">Mail</a>
    <a href="/about-xena">About</a>
    """

    links = extract_links(html, "https://xenaship.com")

    assert "https://xenaship.com/about-xena" in links
    assert len(links) == 1
