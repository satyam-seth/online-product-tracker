from sqlalchemy import ForeignKey, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db import Base, TimestampMixin


class ProductSnapshot(Base, TimestampMixin):
    __tablename__ = "product_snapshots"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id", ondelete="CASCADE"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(String, nullable=True)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    amount: Mapped[float] = mapped_column(Float, nullable=True)
    currency: Mapped[str] = mapped_column(String, nullable=True)

    product: Mapped["Product"] = relationship("Product", back_populates="snapshots")

    def __repr__(self) -> str:
        return (
            f"<ProductSnapshot(id={self.id}, product_id={self.product_id}, "
            f"amount={self.amount}, rating={self.rating}, currency='{self.currency}', "
            f"created_on={self.created_on})>"
        )
