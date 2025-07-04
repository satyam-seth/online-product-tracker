from typing import Optional
from pydantic import BaseModel


class ProductShow(BaseModel):
    title: Optional[str]
    amount: Optional[float]
    currency: Optional[str]
    rating: Optional[float]
    url: str
    source: int


class ProductSnapshotOut(BaseModel):
    id: int
    product_id: int
    title: Optional[str] = None
    rating: Optional[float] = None
    amount: Optional[float] = None
    currency: Optional[str] = None
