# -*- encoding:utf-8 -*-
from sqlalchemy import select
from models.models import Models
from models.schemas.ColorsSchema import ColorsSchema

"""
  ColorsDAO class.
  https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html
"""
class ColorsDAO:
  def __init__(self) -> None:
    self.models = Models()

  def get_color_from_id(self, id: int):
    query = select(ColorsSchema).where(ColorsSchema.id == id)
    row = self.models.session.scalars(query).first()
    return row

  def get_all_colors(self):
    query = select(ColorsSchema)
    all = self.models.session.scalars(query).all()
    return all