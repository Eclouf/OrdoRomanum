# -*- encoding:utf-8 -*-
from sqlalchemy import select
from models.schemas.CategorySchema import CategorySchema
from models.utils.AbstractDAO import AbstractDAO

"""
    CategoryDAO class.
    https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html
"""


class CategoryDAO(AbstractDAO):
    def get_by_id(self, id: int):
        query = select(CategorySchema).where(CategorySchema.id == id)
        row = self.session.scalars(query).first()
        return row

    def get_all(self):
        query = select(CategorySchema)
        all = self.session.scalars(query).all()
        return all
