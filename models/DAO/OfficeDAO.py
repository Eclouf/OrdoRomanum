# -*- encoding:utf-8 -*-
from sqlalchemy import select
from models.schemas.OfficeSchema import OfficeSchema
from models.utils.AbstractDAO import AbstractDAO

"""
    Class to interact with Temporal table in the database making CRUD and extended oprations
    https://en.wikipedia.org/wiki/Create,_read,_update_and_delete
"""


class OfficeDAO(AbstractDAO):
    def get_by_id(self, id: int):
        query = select(OfficeSchema).where(OfficeSchema.id == id)
        row = self.session.scalars(query).all()
        return row
    
    def get_office(self, id: int):
        query = select(OfficeSchema.office).where(OfficeSchema.id == id)
        row = self.session.scalars(query).first()
        return row
    
    def get_matins(self, id: int):
        query = select(OfficeSchema.matins).where(OfficeSchema.id == id)
        row = self.session.scalars(query).first()
        return row
    
    def get_lauds(self, id: int):
        query = select(OfficeSchema.lauds).where(OfficeSchema.id == id)
        row = self.session.scalars(query).first()
        return row
    
    def get_prime(self, id: int):
        query = select(OfficeSchema.prime).where(OfficeSchema.id == id)
        row = self.session.scalars(query).first()
        return row
    
    def get_little_hours(self, id: int):
        query = select(OfficeSchema.little_hours).where(OfficeSchema.id == id)
        row = self.session.scalars(query).first()
        return row
    
    def get_vespers(self, id: int):
        query = select(OfficeSchema.vespers).where(OfficeSchema.id == id)
        row = self.session.scalars(query).first()
        return row
    
    def get_compline(self, id: int):
        query = select(OfficeSchema.compline).where(OfficeSchema.id == id)
        row = self.session.scalars(query).first()
        return row
    
    def get_all(self):
        pass
