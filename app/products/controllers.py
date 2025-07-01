from urllib.parse import urlparse

from fastapi import APIRouter, HTTPException, Response, status

from ..sources.services import get_source_by_domain
from .services import (
    create_product,
    get_product_by_id,
    get_product_by_url,
    list_products,
    delete_product,
)
from .schemas import ProductOut


products_router = APIRouter(prefix="/products", tags=["Products"])


@products_router.post("/", response_model=ProductOut)
async def product_create(url: str):
    # check if product already exists
    existing_product = await get_product_by_url(url)

    # if product already exists, raise an error
    if existing_product:
        raise HTTPException(status_code=409, detail="Product already exists")

    # parse the URL to get the domain and find the source
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.lower()
    source = await get_source_by_domain(domain)

    # if no source is found, raise an error
    if not source:
        raise HTTPException(status_code=400, detail="Website not supported yet")

    # create the product using the source ID and URL
    product = await create_product(url=url, source_id=source.id)
    return product


@products_router.get("/{product_id}", response_model=ProductOut)
async def product_get(product_id: int):
    product = await get_product_by_id(product_id)

    # if product is not found, raise an error
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


# TODO: add support for pagination, filtering by source
@products_router.get("/", response_model=list[ProductOut])
async def product_list():
    products = await list_products()
    return products


@products_router.delete("/{product_id}", response_model=ProductOut)
async def product_delete(product_id: int):
    succeed = await delete_product(product_id)

    if not succeed:
        raise HTTPException(status_code=404, detail="Product not found")

    return Response(status_code=status.HTTP_204_NO_CONTENT)
