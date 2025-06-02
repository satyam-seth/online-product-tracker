from typing import Optional
from pydantic import BaseModel


class SourceCreate(BaseModel):
    name: str
    domain: str
    title_selector: str
    price_selector: str
    rating_selector: str


class SourceUpdate(BaseModel):
    name: Optional[str] = None
    domain: Optional[str] = None
    title_selector: Optional[str] = None
    price_selector: Optional[str] = None
    rating_selector: Optional[str] = None


class SourceOut(SourceCreate):
    id: int
