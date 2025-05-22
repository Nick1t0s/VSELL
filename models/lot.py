from sqlalchemy.orm import mapped_column
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from typing import Optional

from base import Base

from datetime import datetime


class Lot(Base):
    __tablename__ = 'lots'
    id: Mapped[int] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)
    model: Mapped[str] = mapped_column(nullable=False)
    user: Mapped[bool] = mapped_column(nullable=False)
    cost: Mapped[int] = mapped_column(nullable=False)
    place: Mapped[str] = mapped_column(nullable=True)

    statePOD: Mapped[Optional[str]] = mapped_column(nullable=True)
    stateCART: Mapped[Optional[str]] = mapped_column(nullable=True)
    color: Mapped[Optional[str]] = mapped_column(nullable=True)

    puffs: Mapped[Optional[int]] = mapped_column(nullable=True)

    taste: Mapped[Optional[int]] = mapped_column(nullable=True)

    evap: Mapped[Optional[bool]] = mapped_column(nullable=True)
    evapR: Mapped[Optional[str]] = mapped_column(nullable=True)
    stateEvap: Mapped[Optional[str]] = mapped_column(nullable=True)

    stocks: Mapped[Optional[str]] = mapped_column(nullable=True)


