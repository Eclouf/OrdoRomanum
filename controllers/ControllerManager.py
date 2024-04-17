# -*- encoding:utf-8 -*-
from models.models import Models
from controllers.ColorsCtrl import ColorsCtrl
from controllers.CompetitionCtrl import CompetitionCtrl
from controllers.OccurenceCtrl import OccurenceCtrl
from controllers.SanctoralCtrl import SanctoralCtrl
from controllers.TemporalCtrl import TemporalCtrl
from controllers.TranslationCtrl import TranslationCtrl

"""
  ControllerManager initialize the models & allow to retrieve each controllers and instantiate them one time if they aren't
  Each controller has to be imported from here, NEVER OUTSIDE
"""
class ControllerManager:
  _models = Models()
  _colors_ctrl = None
  _competition_ctrl = None
  _occurrence_ctrl = None
  _sanctoral_ctrl = None
  _temporal_ctrl = None
  _translation_ctrl = None
    
  @staticmethod
  def get_colors_ctrl():
    if not ControllerManager._colors_ctrl:
      ControllerManager._colors_ctrl = ColorsCtrl()
    return ControllerManager._colors_ctrl
    
  @staticmethod
  def get_competition_ctrl():
    if not ControllerManager._competition_ctrl:
      ControllerManager._competition_ctrl = CompetitionCtrl()
    return ControllerManager._competition_ctrl
    
  @staticmethod
  def get_occurrence_ctrl():
    if not ControllerManager._occurrence_ctrl:
      ControllerManager._occurrence_ctrl = OccurenceCtrl()
    return ControllerManager._occurrence_ctrl
    
  @staticmethod
  def get_sanctoral_ctrl():
    if not ControllerManager._sanctoral_ctrl:
      ControllerManager._sanctoral_ctrl = SanctoralCtrl()
    return ControllerManager._sanctoral_ctrl
    
  @staticmethod
  def get_temporal_ctrl():
    if not ControllerManager._temporal_ctrl:
      ControllerManager._temporal_ctrl = TemporalCtrl()
    return ControllerManager._temporal_ctrl
    
  @staticmethod
  def get_translation_ctrl():
    if not ControllerManager._translation_ctrl:
      ControllerManager._translation_ctrl = TranslationCtrl()
    return ControllerManager._translation_ctrl
