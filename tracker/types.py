from typing import TypedDict, Optional


class SourceConfig(TypedDict):
    id: int
    name: str
    domain: str
    title_selector: str
    price_selector: str
    rating_selector: str


class ProductData(TypedDict):
    title: Optional[str]
    amount: Optional[float]
    currency: Optional[str]
    rating: Optional[float]
    url: str
    source: int


class ProductHistory(ProductData):
    id: int
    timestamp: str
