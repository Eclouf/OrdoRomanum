# -*- encoding:utf-8 -*-
from models.ModelManager import ModelManager

"""
    Temporal controller.
    Contains logic regarding actions performed by the user about temporal
"""


class TemporalCtrl:
    def __init__(self, model: ModelManager):
        self.dao = model.get_temporal_dao()

    def get_all_fest(self):
        pass

    def get_fest_name(self):
        # return the Feast as dict
        return "Fête de truc"
    
    def get_fest(self):
        pass
