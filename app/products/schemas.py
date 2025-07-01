from pydantic import BaseModel


class ProductOut(BaseModel):
    id: int
    url: str
    source_id: int
