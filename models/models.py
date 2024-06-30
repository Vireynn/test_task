from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text
from .database import Base

class Adverts(Base):
    __table_args__ = {"comment": "Таблица объявлений"}

    advert_id: Mapped[int] = mapped_column(primary_key=True, comment="ID объявления")
    title: Mapped[str] = mapped_column(Text(length=255), nullable=False, comment="Заголовок объявления")
    author: Mapped[str] = mapped_column(Text(length=255), nullable=False, comment="Автор объявления")
    views: Mapped[int] = mapped_column(comment="Количество просмотров")
    position: Mapped[int] = mapped_column(comment="Позиция объявления")
