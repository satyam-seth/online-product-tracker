from typing import TypedDict, Optional


class ScrapePageData(TypedDict):
    title_selector: str
    price_selector: str
    rating_selector: str
    url: str
    source: str

class ProductData(TypedDict):
    title: Optional[str]
    price: Optional[str]
    source: str
    url: str
