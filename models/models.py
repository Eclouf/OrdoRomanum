# -*- encoding:utf-8 -*-
from config import ENV
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.utils.base import Base

# All schemas has to be imported here to create table in database
from models.schemas import ColorsSchema, TemporalSchema, SanctoralSchema, ExceptionsSchema

"""
  singleton pattern: https://refactoring.guru/fr/design-patterns/singleton/python/example
"""
class SingletonModel(type):
  _instances = {}

  def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
      instance = super().__call__(*args, **kwargs)
      cls._instances[cls] = instance
    return cls._instances[cls]

"""
  Singleton Model class. Use to initialize the database
  Difference between normal inheritance vs metaclass inheritance: https://medium.com/@saimun92/difference-between-a-normal-class-inheritance-and-a-metaclass-inheritance-in-python-7bfa26a055ba
"""
class Model(metaclass=SingletonModel):
  engine = create_engine("sqlite:///models/ordo.db", echo=True if ENV == 'dev' else False)
  Session = sessionmaker(bind=engine)
  session = Session()
  Base.metadata.create_all(engine)