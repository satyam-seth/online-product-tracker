from sqlalchemy import String, Index, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db.base import Base
from ..mixin import TimestampMixin


class Product(Base, TimestampMixin):
    __tablename__ = "products"
    __table_args__ = (Index("idx_products_url", "url"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    source_id: Mapped[int] = mapped_column(ForeignKey("sources.id"), nullable=False)

    source: Mapped["Source"] = relationship("Source", back_populates="products")

    def __repr__(self) -> str:
        return f"<Product id={self.id} url={self.url} source_id={self.source_id}>"
