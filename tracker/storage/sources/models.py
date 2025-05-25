from sqlalchemy import String, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db.base import Base
from ..mixin import TimestampMixin


class Source(Base, TimestampMixin):
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

    products: Mapped[list["Product"]] = relationship("Product", back_populates="source")

    def __repr__(self) -> str:
        return f"<Source(id={self.id}, name='{self.name}', domain='{self.domain}')>"
