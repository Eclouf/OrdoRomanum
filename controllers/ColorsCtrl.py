# -*- encoding:utf-8 -*-
from models.ModelManager import ModelManager


"""
  Colors controller.
"""


class ColorsCtrl:
    def __init__(self, model: ModelManager) -> None:
        self.dao = model.get_colors_dao()

    def tests(self):
        rows = self.dao.get_all()

        print("colors_dao.get_all_colors():")
        for row in rows:
            print(f"  {row}")
