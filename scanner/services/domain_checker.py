import json
from pathlib import Path
from url_parser import *


BASE_DIR = Path(__file__).resolve().parents[2]

trusted_domains_path = BASE_DIR / "data" / "trusted_domains.json"

with open(trusted_domains_path, "r") as file:
    trusted_domains = json.load(file)


def is_trusted_domain(parsed_url):
    domain = parsed_url["domain"]
    return domain in trusted_domains

if __name__ == "__main__":
    url = "https://facebook.com/login"
    parsed = parse_url(url)
    print(is_trusted_domain(parsed))