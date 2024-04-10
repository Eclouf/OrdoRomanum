# -*- encoding:utf-8 -*-
from config import ENV
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

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

class Model(metaclass=SingletonModel):
  engine = create_engine("sqlite://", echo=True if ENV == 'dev' else False)
  session = Session(engine)
  Base.metadata.create_all(engine)