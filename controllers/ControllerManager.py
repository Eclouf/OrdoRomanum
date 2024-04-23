# -*- encoding:utf-8 -*-
from models.ModelManager import ModelManager
from controllers.ColorsCtrl import ColorsCtrl
from controllers.ContentsCtrl import ContentsCtrl
from controllers.OccurenceCtrl import OccurenceCtrl
from controllers.SanctoralCtrl import SanctoralCtrl
from controllers.TemporalCtrl import TemporalCtrl
from controllers.TranslationCtrl import TranslationCtrl
from controllers.CalendarCtrl import CalendarRom
from controllers.DioceseCtrl import DioceseCtrl
from controllers.CongregationCtrl import CongregationCtrl
"""
    ControllerManager initialize the models & allow to retrieve each controllers and instantiate them one time if they aren't
    Each controller has to be imported from here, NEVER OUTSIDE
"""


class ControllerManager:
    _model = ModelManager()
    _calendar_ctrl = None
    _colors_ctrl = None
    _contents_ctrl = None
    _occurrence_ctrl = None
    _sanctoral_ctrl = None
    _temporal_ctrl = None
    _translation_ctrl = None
    _diocese_ctrl = None
    _congregation_ctrl = None

    @staticmethod
    def get_colors_ctrl():
        cm = ControllerManager
        if not cm._colors_ctrl:
            cm._colors_ctrl = ColorsCtrl(cm._model)
        return cm._colors_ctrl

    @staticmethod
    def get_contents_ctrl():
        cm = ControllerManager
        if not cm._contents_ctrl:
            cm._contents_ctrl = ContentsCtrl()
        return cm._contents_ctrl

    @staticmethod
    def get_occurrence_ctrl():
        cm = ControllerManager
        if not cm._occurrence_ctrl:
            cm._occurrence_ctrl = OccurenceCtrl()
        return cm._occurrence_ctrl

    @staticmethod
    def get_sanctoral_ctrl():
        cm = ControllerManager
        if not cm._sanctoral_ctrl:
            cm._sanctoral_ctrl = SanctoralCtrl(cm._model)
        return cm._sanctoral_ctrl

    @staticmethod
    def get_temporal_ctrl():
        cm = ControllerManager
        if not cm._temporal_ctrl:
            cm._temporal_ctrl = TemporalCtrl(cm._model)
        return cm._temporal_ctrl

    @staticmethod
    def get_translation_ctrl():
        cm = ControllerManager
        if not cm._translation_ctrl:
            cm._translation_ctrl = TranslationCtrl()
        return cm._translation_ctrl

    @staticmethod
    def get_calendar_ctrl():
        cm = ControllerManager
        if not cm._calendar_ctrl:
            cm._calendar_ctrl = CalendarRom()
        return cm._calendar_ctrl
    
    @staticmethod
    def get_diocese_ctrl():
        cm = ControllerManager
        if not cm._diocese_ctrl:
            cm._diocese_ctrl = DioceseCtrl()
        return cm._diocese_ctrl
    
    @staticmethod
    def get_congregation_ctrl():
        cm = ControllerManager
        if not cm._congregation_ctrl:
            cm._congregation_ctrl = CongregationCtrl()
        return cm._congregation_ctrl
