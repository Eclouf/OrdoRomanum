# -*- encoding:utf-8 -*-
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ARRAY, ForeignKey
from models.models import Base

class ExceptionsSchema(Base):
  __tablename__ = "exceptions"
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  exception: Mapped[str] = mapped_column(String)
  

  def __repr__(self) -> str:
    return f"ExceptionsSchema(id={self.id!r}, exception={self.exception!r})"