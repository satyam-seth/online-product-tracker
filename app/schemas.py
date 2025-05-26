from typing import TypedDict, Optional

from pydantic import BaseModel


class HealthCheck(BaseModel):
    status: str = "healthy"


# TODO: use pydentic
class ProductData(TypedDict):
    title: Optional[str]
    amount: Optional[float]
    currency: Optional[str]
    rating: Optional[float]
    url: str
    source: int
