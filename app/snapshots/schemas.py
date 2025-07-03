from typing import Optional
from pydantic import BaseModel


class ProductShow(BaseModel):
    title: Optional[str]
    amount: Optional[float]
    currency: Optional[str]
    rating: Optional[float]
    url: str
    source: int


# ek snapshot fetch api bayenge wha se bus fetch karke dikha denge
# fir ek histoty api bna denge
