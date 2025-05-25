from typing import Optional, Sequence
from sqlalchemy import select
from tracker.storage.products.models import Product
from tracker.storage.db.config import async_session


async def create_product(
    url: str,
    source_id: int,
) -> Product:
    async with async_session() as session:
        product = Product(url=url, source_id=source_id)
        session.add(product)
        await session.commit()
        await session.refresh(product)
        return product


async def get_product_by_id(product_id: int) -> Optional[Product]:
    async with async_session() as session:
        product = await session.get(Product, product_id)
        return product


async def get_product_by_url(url: str) -> Optional[Product]:
    async with async_session() as session:
        stmt = select(Product).where(Product.url == url)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()


async def list_products() -> Sequence[Product]:
    async with async_session() as session:
        stmt = select(Product)
        product = await session.scalars(stmt)
        return product.all()


async def update_product(
    product_id: int,
    url: Optional[str] = None,
    source_id: Optional[int] = None,
) -> Optional[Product]:
    async with async_session() as session:
        product = await session.get(Product, product_id)

        if not product:
            return None

        if url is not None:
            product.url = url
        if source_id is not None:
            product.source_id = source_id

        await session.commit()
        await session.refresh(product)
        return product


async def delete_product(product_id: int) -> bool:
    async with async_session() as session:
        product = await session.get(Product, product_id)

        if not product:
            return False

        await session.delete(product)
        await session.commit()
        return True
