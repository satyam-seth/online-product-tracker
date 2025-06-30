from fastapi import APIRouter

from app.fetcher import fetch_product_details

from .schemas import ProductShow


snapshots_router = APIRouter(prefix="/snapshots", tags=["Snapshots"])


@snapshots_router.post("/", response_model=ProductShow)
async def snapshot_create(url: str):
    source = await fetch_product_details(url)
    return source
