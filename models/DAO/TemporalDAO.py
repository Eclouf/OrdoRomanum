# -*- encoding:utf-8 -*-
from sqlalchemy import select
from models.models import Models

"""
  Class to interact with Temporal table in the database making CRUD and extended oprations
  https://en.wikipedia.org/wiki/Create,_read,_update_and_delete
"""
class TemporalDAO:
  def __init__(self) -> None:
    self.models = Models()