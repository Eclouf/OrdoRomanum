# -*- encoding:utf-8 -*-
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from models.utils.Base import Base


class CategorySchema(Base):
    __tablename__ = "category"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    category: Mapped[str] = mapped_column(String)

    def __repr__(self) -> str:
        return f"CategorySchema(id={self.id!r}, category={self.category!r})"
