from urllib.parse import urlparse


def parse_url(url):
    url = norm_url(url)
    parsed = urlparse(url)

    return {
        "url":url,
        "scheme": parsed.scheme,
        "domain": parsed.hostname,
        "port": parsed.port,
        "path": parsed.path,
        "query": parsed.query,
        "fragment": parsed.fragment,
    }

def norm_url(url):
    url = url.strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    return url


if __name__ == "__main__":
    url = "https://example.com:8080/login?user=123#section"

    result = parse_url(url)

    for key, value in result.items():
        print(f"{key}: {value}")