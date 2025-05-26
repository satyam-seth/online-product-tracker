from typing import Optional, Sequence
from sqlalchemy import select
from ..db.config import async_session

from .models import Source
from .schemas import SourceCreate


async def create_source(new_source: SourceCreate) -> Source:
    async with async_session() as session:
        source = Source(
            name=new_source.name,
            domain=new_source.domain,
            title_selector=new_source.title_selector,
            price_selector=new_source.price_selector,
            rating_selector=new_source.rating_selector,
        )
        session.add(source)
        await session.commit()
        await session.refresh(source)
        return source


async def get_source_by_id(source_id: int) -> Optional[Source]:
    async with async_session() as session:
        source = await session.get(Source, source_id)
        return source


async def get_source_by_domain(domain: str) -> Optional[Source]:
    async with async_session() as session:
        stmt = select(Source).where(Source.domain == domain)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()


async def list_sources() -> Sequence[Source]:
    async with async_session() as session:
        stmt = select(Source)
        sources = await session.scalars(stmt)
        return sources.all()


async def update_source(
    source_id: int,
    name: Optional[str] = None,
    domain: Optional[str] = None,
    title_selector: Optional[str] = None,
    price_selector: Optional[str] = None,
    rating_selector: Optional[str] = None,
) -> Optional[Source]:
    async with async_session() as session:
        source = await session.get(Source, source_id)

        if not source:
            return None

        if name is not None:
            source.name = name
        if domain is not None:
            source.domain = domain
        if title_selector is not None:
            source.title_selector = title_selector
        if price_selector is not None:
            source.price_selector = price_selector
        if rating_selector is not None:
            source.rating_selector = rating_selector

        await session.commit()
        return source


async def delete_source(source_id: int) -> bool:
    async with async_session() as session:
        source = await session.get(Source, source_id)

        if not source:
            return False

        await session.delete(source)
        await session.commit()
        return True
