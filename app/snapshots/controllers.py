from fastapi import APIRouter, HTTPException

from app.exceptions import WebsiteNotSupportedError
from app.fetcher import fetch_product_details
from .services import list_snapshots, list_snapshots_for_product
from .schemas import ProductShow, ProductSnapshotOut


snapshots_router = APIRouter(prefix="/snapshots", tags=["Snapshots"])


@snapshots_router.post("/fetch", response_model=ProductShow)
async def snapshot_fetch(url: str):
    try:
        source = await fetch_product_details(url)
        return source
    except WebsiteNotSupportedError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@snapshots_router.get("/", response_model=list[ProductSnapshotOut])
async def snapshot_list(product_id: int | None = None):
    if product_id is None:
        return await list_snapshots()
    return await list_snapshots_for_product(product_id)
