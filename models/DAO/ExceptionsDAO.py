# -*- encoding:utf-8 -*-
from sqlalchemy import select
from models.schemas.ExceptionsSchema import ExceptionsSchema
from models.utils.AbstractDAO import AbstractDAO

"""
    ColorsDAO class.
    https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html
"""


class ExceptionsDAO(AbstractDAO):
    def get_by_id(self, id: int):
        query = select(ExceptionsSchema).where(ExceptionsSchema.id == id)
        row = self.session.scalars(query).first()
        return row

    def get_all(self):
        query = select(ExceptionsSchema)
        all = self.session.scalars(query).all()
        return all
