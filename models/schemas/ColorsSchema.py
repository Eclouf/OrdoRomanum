# -*- encoding:utf-8 -*-
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from models.utils.Base import Base

class ColorsSchema(Base):
  __tablename__ = "colors"
  id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
  name: Mapped[str] = mapped_column(String)

  def __repr__(self) -> str:
    return f"ColorsSchema(id={self.id!r}, name={self.name!r})"
