# -*- encoding:utf-8 -*-
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from models.utils.Base import Base


class OfficeSchema(Base):
    __tablename__ = "office"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    office: Mapped[str] = mapped_column(String)
    matins: Mapped[str] = mapped_column(String)
    lauds: Mapped[str] = mapped_column(String)
    prime: Mapped[str] = mapped_column(String)
    little_hours: Mapped[str] = mapped_column(String)
    vespers: Mapped[str] = mapped_column(String)
    compline: Mapped[str] = mapped_column(String)
    
def __repr__(self) -> str:
        return f"OfficeSchema(id={self.id!r}, office={self.office!r}, matins={self.matins!r}, lauds={self.lauds!r} prime={self.prime!r}, little_hours={self.little_hours!r}, vespers={self.vespers!r}, compline={self.compline!r})"
