# -*- encoding:utf-8 -*-
from sqlalchemy import select
from models.schemas.ColorsSchema import ColorsSchema
from models.utils.AbstractDAO import AbstractDAO

"""
  ColorsDAO class.
  https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html
"""
class ColorsDAO(AbstractDAO):
  def get_by_id(self, id: int):
    query = select(ColorsSchema).where(ColorsSchema.id == id)
    row = self.session.scalars(query).first()
    return row

  def get_all(self):
    query = select(ColorsSchema)
    all = self.session.scalars(query).all()
    return all