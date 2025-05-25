from typing import Optional, Sequence
from sqlalchemy import select

from ..db.config import async_session
from .models import ProductSnapshot


async def create_snapshot(
    product_id: int,
    title: Optional[str] = None,
    rating: Optional[float] = None,
    amount: Optional[float] = None,
    currency: Optional[str] = None,
) -> ProductSnapshot:
    async with async_session() as session:
        snapshot = ProductSnapshot(
            product_id=product_id,
            title=title,
            rating=rating,
            amount=amount,
            currency=currency,
        )
        session.add(snapshot)
        await session.commit()
        await session.refresh(snapshot)
        return snapshot


async def get_snapshot_by_id(snapshot_id: int) -> Optional[ProductSnapshot]:
    async with async_session() as session:
        return await session.get(ProductSnapshot, snapshot_id)


async def list_snapshots() -> Sequence[ProductSnapshot]:
    async with async_session() as session:
        stmt = select(ProductSnapshot)
        result = await session.execute(stmt)
        return result.scalars().all()


async def list_snapshots_for_product(product_id: int) -> Sequence[ProductSnapshot]:
    async with async_session() as session:
        stmt = select(ProductSnapshot).where(ProductSnapshot.product_id == product_id)
        result = await session.execute(stmt)
        return result.scalars().all()


async def update_snapshot(
    snapshot_id: int,
    title: Optional[str] = None,
    rating: Optional[float] = None,
    amount: Optional[float] = None,
    currency: Optional[str] = None,
) -> Optional[ProductSnapshot]:
    async with async_session() as session:
        snapshot = await session.get(ProductSnapshot, snapshot_id)

        if not snapshot:
            return None
        if title is not None:
            snapshot.title = title
        if rating is not None:
            snapshot.rating = rating
        if amount is not None:
            snapshot.amount = amount
        if currency is not None:
            snapshot.currency = currency

        await session.commit()
        await session.refresh(snapshot)
        return snapshot


async def delete_snapshot(snapshot_id: int) -> bool:
    async with async_session() as session:
        snapshot = await session.get(ProductSnapshot, snapshot_id)

        if not snapshot:
            return False

        await session.delete(snapshot)
        await session.commit()
        return True
