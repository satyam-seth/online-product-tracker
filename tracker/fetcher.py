import random
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

from tracker.types import ProductData

USER_AGENTS = [  # Rotate to avoid blocks
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)...",
]

HEADERS = {
    "User-Agent": random.choice(USER_AGENTS),
    "Accept-Language": "en-US,en;q=0.9",
}

def scrape_amazon(url: str) -> ProductData:
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.text, "html.parser")

    title = soup.select_one("#productTitle")
    price = soup.select_one(".priceToPay")
    rating = soup.select_one("#acrPopover > span > a > span")

    return {
        "title": title.get_text(strip=True) if title else None,
        "price": price.get_text(strip=True) if price else None,
        "rating": rating.get_text(strip=True) if rating else None,
        "url": url,
        "source": "amazon",
    }

def scrape_flipkart(url: str) -> ProductData:
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.text, "html.parser")

    title = soup.select_one(".C7fEHH .VU-ZEz")
    price = soup.select_one(".C7fEHH .Nx9bqj.CxhGGd")
    rating = soup.select_one(".C7fEHH .XQDdHH")

    return {
        "title": title.get_text(strip=True) if title else None,
        "price": price.get_text(strip=True) if price else None,
        "rating": rating.get_text(strip=True) if rating else None,
        "url": url,
        "source": "flipkart",
    }

def fetch_product_details(url: str) -> dict:
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.lower()

    if "amazon." in domain:
        return scrape_amazon(url)
    
    elif "flipkart." in domain:
        return scrape_flipkart(url)
    
    else:
        raise ValueError("Website not supported yet")