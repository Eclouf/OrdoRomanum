# -*- encoding:utf-8 -*-
from models.ModelManager import TypeModelManager


"""
  Temporal controller.
  Contains logic regarding actions performed by the user about temporal
"""
class SanctoralCtrl:
  def __init__(self, model: TypeModelManager):
    self.dao = model.get_sanctoral_dao()

  def get_all_fest(self):
    pass

  def get_fest_name(self):
    return "Fête de truc"