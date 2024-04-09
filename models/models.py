# -*- encoding:utf-8 -*-
from main import ENV
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

class Model:
  engine = create_engine("sqlite://", echo=True if ENV == 'dev' else False)
  session = Session(engine)
  Base.metadata.create_all(engine)