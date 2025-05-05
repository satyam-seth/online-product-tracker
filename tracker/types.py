from typing import TypedDict, Optional
from enum import IntEnum


class Source(IntEnum):
    AMAZON = 1
    FLIPKART = 2

class ScrapePageData(TypedDict):
    title_selector: str
    price_selector: str
    rating_selector: str
    url: str
    source: str

class ProductData(TypedDict):
    url: str
    title: Optional[str]
    amount: Optional[float] 
    currency: Optional[str]
    rating: Optional[float]
    source: Source
