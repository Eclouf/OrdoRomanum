# -*- encoding:utf-8 -*-
from models.DAO.TemporalDAO import TemporalDAO

"""
  Temporal controller.
  Contains logic regarding actions performed by the user about temporal
"""
class TemporalCtrl():
  def __init__(self):
    self.temporal_dao = TemporalDAO()

  def getAllFest(self):
    pass

  def getFestName(self):
    return "Fête de truc"