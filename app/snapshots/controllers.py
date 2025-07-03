from fastapi import APIRouter, HTTPException

from app.exceptions import WebsiteNotSupportedError
from app.fetcher import fetch_product_details

from .schemas import ProductShow


snapshots_router = APIRouter(prefix="/snapshots", tags=["Snapshots"])


@snapshots_router.post("/fetch", response_model=ProductShow)
async def snapshot_fetch(url: str):
    try:
        source = await fetch_product_details(url)
        return source
    except WebsiteNotSupportedError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
