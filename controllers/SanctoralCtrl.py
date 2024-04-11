# -*- encoding:utf-8 -*-
from models.DAO.SanctoralDAO import SanctoralDAO

"""
  Temporal controller.
  Contains logic regarding actions performed by the user about temporal
"""
class SanctoralCtrl():
  def __init__(self):
    self.SanctoralDAO = SanctoralDAO

  def getAllFest(self):
    pass

  def getFestName(self):
    return "Fête de truc"