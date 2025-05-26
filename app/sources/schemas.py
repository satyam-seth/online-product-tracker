from pydantic import BaseModel


class SourceCreate(BaseModel):
    name: str
    domain: str
    title_selector: str
    price_selector: str
    rating_selector: str


class SourceOut(SourceCreate):
    id: int
