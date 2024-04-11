# -*- encoding:utf-8 -*-
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ARRAY
from models.utils.base import Base

class ExecpetionsSchema(Base):
  __tablename__ = "execptions"
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  exception: Mapped[str] = mapped_column(String)
  

  def __repr__(self) -> str:
    return f"ExeceptionsSchema(id={self.id!r}, execptions={self.exception!r}"