from typing import Optional, Sequence
from sqlalchemy import select
from ..db.config import async_session

from .models import Source
from .schemas import SourceCreate, SourceUpdate


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
    updated_source: SourceUpdate,
) -> Optional[Source]:
    async with async_session() as session:
        source = await session.get(Source, source_id)

        if not source:
            return None

        if updated_source.name is not None:
            source.name = updated_source.name
        if updated_source.domain is not None:
            source.domain = updated_source.domain
        if updated_source.title_selector is not None:
            source.title_selector = updated_source.title_selector
        if updated_source.price_selector is not None:
            source.price_selector = updated_source.price_selector
        if updated_source.rating_selector is not None:
            source.rating_selector = updated_source.rating_selector

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
