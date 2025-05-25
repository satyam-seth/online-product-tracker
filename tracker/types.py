from typing import TypedDict, Optional


class ProductData(TypedDict):
    title: Optional[str]
    amount: Optional[float]
    currency: Optional[str]
    rating: Optional[float]
    url: str
    source: int
