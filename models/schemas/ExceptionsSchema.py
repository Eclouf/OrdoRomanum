# -*- encoding:utf-8 -*-
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ARRAY, ForeignKey
from models.models import Base

class ExecpetionsSchema(Base):
  __tablename__ = "execptions"
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  exceptions: Mapped[str] = mapped_column(String)
  

  def __repr__(self) -> str:
    return f"ExeceptionsSchema(id={self.id!r}, execptions={self.exceptions!r}"