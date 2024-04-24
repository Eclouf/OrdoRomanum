# -*- encoding:utf-8 -*-
from sqlalchemy import select
from models.schemas.SanctoralSchema import SanctoralSchema
from models.utils.AbstractDAO import AbstractDAO

"""
    Class to interact with Temporal table in the database making CRUD and extended oprations
    https://en.wikipedia.org/wiki/Create,_read,_update_and_delete
"""


class SanctoralDAO(AbstractDAO):
    def get_by_id(self, month: int, day: int):
        query = select(SanctoralSchema).where(SanctoralSchema.index_month == month, SanctoralSchema.index_day == day)
        row = self.session.scalars(query).all()
        return row

    def get_all(self):
        pass
