from sqlalchemy.orm import mapped_column
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from typing import Optional

from base import Base

from datetime import datetime


class Lot(Base):
    __tablename__ = 'lots'
    id: Mapped[int] = mapped_column(primary_key=True) # id
    created: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False) # Дата создания
    type: Mapped[str] = mapped_column(nullable=False) # Тип
    model: Mapped[str] = mapped_column(nullable=False) # Модель
    used: Mapped[bool] = mapped_column(nullable=False) # Б/у
    cost: Mapped[int] = mapped_column(nullable=False) # Цена
    place: Mapped[str] = mapped_column(nullable=True) # Места встречи
    description: Mapped[str] = mapped_column(nullable=True)
    user: Mapped[bool] = mapped_column(nullable=False) # id пользователя


