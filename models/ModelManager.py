# -*- encoding:utf-8 -*-
from config import ENV, STORAGE_BACKEND
from models.utils.Singleton import Singleton

# Import SQL stack only if needed
if STORAGE_BACKEND == 'sqlite':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from models.DAO.SanctoralDAO import SanctoralDAO
    from models.DAO.ColorsDAO import ColorsDAO
    from models.DAO.TemporalDAO import TemporalDAO
    from models.DAO.CategoryDAO import CategoryDAO
    from models.DAO.OfficeDAO import OfficeDAO
    from models.DAO.ExceptionsDAO import ExceptionsDAO
    from models.utils.Base import Base
else:
    # File-based DAOs
    from models.DAO_File.DioceseFileDAO import DioceseFileDAO
    from models.DAO_File.CategoryFileDAO import CategoryFileDAO
    from models.DAO_File.ColorsFileDAO import ColorsFileDAO
    from models.DAO_File.SanctoralFileDAO import SanctoralFileDAO
    from models.DAO_File.OfficeFileDAO import OfficeFileDAO
    from models.DAO_File.TemporalFileDAO import TemporalFileDAO

# All schemas has to be imported here to create table in database
if STORAGE_BACKEND == 'sqlite':
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
        if STORAGE_BACKEND == 'sqlite':
            self.engine = create_engine(
                "sqlite:///models/ordo.db", echo=True if ENV == "dev" else False
            )
            Session = sessionmaker(bind=self.engine)
            self.session = Session()
            Base.metadata.create_all(self.engine)
        else:
            # File backend does not need a DB session
            self.engine = None
            self.session = None

    def get_colors_dao(self):
        if not ModelManager._colors_dao:
            if STORAGE_BACKEND == 'sqlite':
                ModelManager._colors_dao = ColorsDAO(self)
            else:
                ModelManager._colors_dao = ColorsFileDAO(self)
        return ModelManager._colors_dao

    def get_sanctoral_dao(self):
        if not ModelManager._sanctoral_dao:
            if STORAGE_BACKEND == 'sqlite':
                ModelManager._sanctoral_dao = SanctoralDAO(self)
            else:
                ModelManager._sanctoral_dao = SanctoralFileDAO(self)
        return ModelManager._sanctoral_dao

    def get_temporal_dao(self):
        if not ModelManager._temporal_dao:
            if STORAGE_BACKEND == 'sqlite':
                ModelManager._temporal_dao = TemporalDAO(self)
            else:
                ModelManager._temporal_dao = TemporalFileDAO(self)
        return ModelManager._temporal_dao
    
    def get_category_dao(self):
        if not ModelManager._category_dao:
            if STORAGE_BACKEND == 'sqlite':
                ModelManager._category_dao = CategoryDAO(self)
            else:
                ModelManager._category_dao = CategoryFileDAO(self)
        return ModelManager._category_dao
    
    def get_office_dao(self):
        if not ModelManager._office_dao:
            if STORAGE_BACKEND == 'sqlite':
                ModelManager._office_dao = OfficeDAO(self)
            else:
                ModelManager._office_dao = OfficeFileDAO(self)
        return ModelManager._office_dao
    
    def get_exceptions_dao(self):
        if not ModelManager._exceptions_dao:
            if STORAGE_BACKEND == 'sqlite':
                ModelManager._exceptions_dao = ExceptionsDAO(self)
            else:
                ModelManager._exceptions_dao = None
        return ModelManager._exceptions_dao

    def get_diocese_dao(self):
        if not ModelManager._diocese_dao:
           ModelManager._diocese_dao = DioceseFileDAO(self)
        return ModelManager._diocese_dao
        