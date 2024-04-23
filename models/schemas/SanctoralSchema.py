# -*- encoding:utf-8 -*-
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from models.utils.Base import Base


class SanctoralSchema(Base):
    __tablename__ = "sanctoral"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    index_month: Mapped[int] = mapped_column(Integer)
    index_day: Mapped[int] = mapped_column(Integer)
    title: Mapped[str] = mapped_column(String)
    color: Mapped[str] = mapped_column(String)
    office: Mapped[str] = mapped_column(String)
    mass: Mapped[str] = mapped_column(String)
    note: Mapped[str] = mapped_column(String)
    degree: Mapped[str] = mapped_column(String)
    rank: Mapped[int] = mapped_column(Integer)
    occ: Mapped[int] = mapped_column(String)
    con: Mapped[str] = mapped_column(String)

    def __repr__(self) -> str:
        return f"SanctoralSchema(id={self.id!r}, index_month={self.index_month!r}, index_day={self.index_day!r}, title={self.title!r}, color={self.color!r}, office={self.office!r}, mass={self.mass!r}, note={self.note!r}, degree={self.degree!r}, rank={self.rank!r})"
