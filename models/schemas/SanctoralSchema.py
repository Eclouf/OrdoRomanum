# -*- encoding:utf-8 -*-
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ARRAY, ForeignKey
from models.models import Base

class SanctoralSchema(Base):
  __tablename__ = "sanctoral"
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  title: Mapped[str] = mapped_column(String)
  color: Mapped[list[int]] = mapped_column(ARRAY(ForeignKey("colors.id")))
  office: Mapped[str] = mapped_column(String)
  mass: Mapped[str] = mapped_column(String)
  note: Mapped[str] = mapped_column(String)
  degree: Mapped[str] = mapped_column(String)
  rank: Mapped[int] = mapped_column(Integer)

  def __repr__(self) -> str:
    return f"SanctoralSchema(id={self.id!r}, title={self.title!r}, color={self.color!r}"