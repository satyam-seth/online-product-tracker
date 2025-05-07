import random
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from tracker.types import Source, ProductData, ScrapePageData
from tracker.utils import parse_price_with_currency

USER_AGENTS = [  # Rotate to avoid blocks
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)...",
]

HEADERS = {
    "User-Agent": random.choice(USER_AGENTS),
    "Accept-Language": "en-US,en;q=0.9",
}


def scrape_page(data: ScrapePageData) -> ProductData:
    res = requests.get(data["url"], headers=HEADERS, timeout=20)
    soup = BeautifulSoup(res.text, "html.parser")

    title = soup.select_one(data["title_selector"])
    price = soup.select_one(data["price_selector"])
    rating = soup.select_one(data["rating_selector"])

    amount = None
    currency = None

    if price:
        try:
            amount, currency = parse_price_with_currency(price.get_text(strip=True))
        except ValueError:
            # TODO: add logging
            print(f"Failed to parse price: {price.get_text(strip=True)}")

    return {
        "title": title.get_text(strip=True) if title else None,
        "currency": currency,
        "amount": amount,
        "rating": float(rating.get_text(strip=True)) if rating else None,
        "url": data["url"],
        "source": data["source"],
    }


def scrape_amazon(url: str) -> ProductData:

    data: ScrapePageData = {
        "title_selector": "#productTitle",
        "price_selector": ".priceToPay",
        "rating_selector": "#acrPopover > span > a > span",
        "url": url,
        "source": Source.AMAZON,
    }

    return scrape_page(data)


def scrape_flipkart(url: str) -> ProductData:
    data: ScrapePageData = {
        "title_selector": ".C7fEHH .VU-ZEz",
        "price_selector": ".C7fEHH .Nx9bqj.CxhGGd",
        "rating_selector": ".C7fEHH .XQDdHH",
        "url": url,
        "source": Source.FLIPKART,
    }

    return scrape_page(data)


def fetch_product_details(url: str) -> ProductData:
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.lower()

    if "amazon." in domain:
        return scrape_amazon(url)

    if "flipkart." in domain:
        return scrape_flipkart(url)

    raise ValueError("Website not supported yet")
