import random
from urllib.parse import urlparse
from httpx import AsyncClient

from bs4 import BeautifulSoup
from tracker.storage.sources.models import Source
from tracker.storage.sources.services import get_source_by_domain
from tracker.types import ProductData
from tracker.utils import parse_price_with_currency

USER_AGENTS = [  # Rotate to avoid blocks
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)...",
]


def get_headers() -> dict:
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept-Language": "en-US,en;q=0.9",
    }


async def scrape_page(url: str, config: Source) -> ProductData:
    async with AsyncClient(timeout=20) as client:
        res = await client.get(url, headers=get_headers())
        res.raise_for_status()

    print("status_code", res.status_code)
    # print(res.text)

    soup = BeautifulSoup(res.text, "html.parser")
    title = soup.select_one(config.title_selector)
    price = soup.select_one(config.price_selector)
    rating = soup.select_one(config.rating_selector)

    amount = None
    currency = None

    if price:
        try:
            amount, currency = parse_price_with_currency(price.get_text(strip=True))
        except ValueError:
            # TODO: add logging
            print(f"Failed to parse price: {price.get_text(strip=True)}")

    return ProductData(
        title=title.get_text(strip=True) if title else None,
        currency=currency,
        amount=amount,
        rating=float(rating.get_text(strip=True)) if rating else None,
        url=url,
        source=config.id,
    )


async def fetch_product_details(url: str) -> ProductData:
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.lower()

    config = await get_source_by_domain(domain)
    print("config", config)

    if config:
        return await scrape_page(url, config)

    raise ValueError("Website not supported yet")
