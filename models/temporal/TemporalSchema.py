# -*- encoding:utf-8 -*-
from sqlalchemy.orm import Mapped, mapped_column
from models.models import Base


class TemporalSchema(Base):
  __tablename__ = "temporal"
  id: Mapped[int] = mapped_column(primary_key=True)