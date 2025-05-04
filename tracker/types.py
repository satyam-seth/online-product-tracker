from typing import TypedDict, Optional


class ProductData(TypedDict):
    title: Optional[str]
    price: Optional[str]
    source: str
    url: str