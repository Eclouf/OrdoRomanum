# -*- encoding:utf-8 -*-
from typing import TypeVar
from config import ENV
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.DAO.SanctoralDAO import SanctoralDAO
from models.DAO.ColorsDAO import ColorsDAO
from models.DAO.TemporalDAO import TemporalDAO
from models.utils.base import Base
from models.utils.Singleton import Singleton

# All schemas has to be imported here to create table in database
from models.schemas import ColorsSchema, TemporalSchema, SanctoralSchema, ExceptionsSchema

TypeModelManager = TypeVar('TypeModelManager', bound='ModelManager')


"""
  Singleton Model class. Use to initialize the database
  normal inheritance vs metaclass inheritance: https://medium.com/@saimun92/difference-between-a-normal-class-inheritance-and-a-metaclass-inheritance-in-python-7bfa26a055ba
"""
class ModelManager(metaclass=Singleton):
  _colors_dao = None
  _sanctoral_dao = None
  _temporal_dao = None
  
  def __init__(self) -> None:
    self.engine = create_engine("sqlite:///models/ordo.db", echo=True if ENV == 'dev' else False)
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
