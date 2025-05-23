from datetime import datetime
from sqlalchemy import String, Index, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from ..db.base import Base


class Source(Base):
    __tablename__ = "sources"
    __table_args__ = (
        Index("idx_sources_domain", "domain"),
        Index("idx_sources_name", "name"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    domain: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    title_selector: Mapped[str] = mapped_column(String, nullable=False)
    price_selector: Mapped[str] = mapped_column(String, nullable=False)
    rating_selector: Mapped[str] = mapped_column(String, nullable=False)
    created_on: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=func.now(),
    )
    updated_on: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=func.now(),
        onupdate=func.now(),
    )

    def __repr__(self) -> str:
        return f"<Source(id={self.id}, name='{self.name}', domain='{self.domain}')>"
