# -*- encoding:utf-8 -*-
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from models.utils.Base import Base


class TemporalSchema(Base):
    __tablename__ = "temporal"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    color: Mapped[str] = mapped_column(String)
    office: Mapped[str] = mapped_column(String)
    mass: Mapped[str] = mapped_column(String)
    note: Mapped[str] = mapped_column(String)
    degree: Mapped[str] = mapped_column(String)
    feria: Mapped[Optional[str]] = mapped_column(String)
    rank: Mapped[int] = mapped_column(Integer)
    occ: Mapped[int] = mapped_column(String)
    con: Mapped[str] = mapped_column(String)

    def __repr__(self) -> str:
        return f"TemporalSchema(id={self.id!r}, title={self.title!r}, color={self.color!r}, office={self.office!r}, mass={self.mass!r}, note={self.note!r}, degree={self.degree!r}, ferie={self.feria!r}, rank={self.rank!r}, occ={self.occ!r}, con={self.con!r})"
