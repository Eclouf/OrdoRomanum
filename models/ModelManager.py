# -*- encoding:utf-8 -*-
from config import ENV
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.DAO.SanctoralDAO import SanctoralDAO
from models.DAO.ColorsDAO import ColorsDAO
from models.DAO.TemporalDAO import TemporalDAO
from models.DAO.CategoryDAO import CategoryDAO
from models.DAO.OfficeDAO import OfficeDAO
from models.DAO.ExceptionsDAO import ExceptionsDAO
from models.utils.Base import Base
from models.utils.Singleton import Singleton

# All schemas has to be imported here to create table in database
from models.schemas import (
    ColorsSchema,
    TemporalSchema,
    SanctoralSchema,
    ExceptionsSchema,
    CategorySchema,
    OfficeSchema,
)


"""
    Singleton Model class. Use to initialize the database
    normal inheritance vs metaclass inheritance: https://medium.com/@saimun92/difference-between-a-normal-class-inheritance-and-a-metaclass-inheritance-in-python-7bfa26a055ba
"""


class ModelManager(metaclass=Singleton):
    _colors_dao = None
    _sanctoral_dao = None
    _temporal_dao = None
    _category_dao = None
    _office_dao = None
    _exceptions_dao = None

    def __init__(self) -> None:
        self.engine = create_engine(
            "sqlite:///models/ordo.db", echo=True if ENV == "dev" else False
        )
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        Base.metadata.create_all(self.engine)

    def get_colors_dao(self):
        if not ModelManager._colors_dao:
            ModelManager._colors_dao = ColorsDAO(self)
        return ModelManager._colors_dao

    def get_sanctoral_dao(self):
        if not ModelManager._sanctoral_dao:
            ModelManager._sanctoral_dao = SanctoralDAO(self)
        return ModelManager._sanctoral_dao

    def get_temporal_dao(self):
        if not ModelManager._temporal_dao:
            ModelManager._temporal_dao = TemporalDAO(self)
        return ModelManager._temporal_dao
    
    def get_category_dao(self):
        if not ModelManager._category_dao:
            ModelManager._category_dao = CategoryDAO(self)
        return ModelManager._category_dao
    
    def get_office_dao(self):
        if not ModelManager._office_dao:
            ModelManager._office_dao = OfficeDAO(self)
        return ModelManager._office_dao
    
    def get_exceptions_dao(self):
        if not ModelManager._exceptions_dao:
            ModelManager._exceptions_dao = ExceptionsDAO(self)
        return ModelManager._exceptions_dao
