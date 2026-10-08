from url_parser import parse_url

def extract_features(parsed_url):
    domain = parsed_url["domain"]

    features={
        "uses_https": parsed_url["scheme"] == "https",
        "url_length": len(parsed_url["url"]),
        "domain_length": len(domain),
    }

    return features

if __name__ == "__main__":
    url = "https://example.com:8080/login?user=123#section"
    parsed = parse_url(url)

    print(extract_features(parsed))