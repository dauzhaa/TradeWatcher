from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Numeric, BigInteger, String
from decimal import Decimal
from src.core.base import Base

class Candle(Base):
    __tablename__ = "analytic_candles"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    start_time: Mapped[int] = mapped_column(BigInteger, nullable=False)
    symbol: Mapped[str] = mapped_column(String, nullable=False)
    interval: Mapped[str] = mapped_column(String, nullable=False)
    open_price: Mapped[Decimal] = mapped_column(Numeric(20, 8))
    close_price: Mapped[Decimal] = mapped_column(Numeric(20, 8))
    high_price: Mapped[Decimal] = mapped_column(Numeric(20, 8))
    low_price: Mapped[Decimal] = mapped_column(Numeric(20, 8))
    volume: Mapped[Decimal] = mapped_column(Numeric(20, 8))
    
    