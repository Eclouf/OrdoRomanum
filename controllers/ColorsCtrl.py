# -*- encoding:utf-8 -*-
from models.DAO.ColorsDAO import ColorsDAO


"""
  Colors controller.
"""
class ColorsCtrl:
  def __init__(self) -> None:
    self.colors_dao = ColorsDAO()

  def tests(self):
    rows = self.colors_dao.get_all_colors()

    print('colors_dao.get_all_colors():')
    for row in rows:
      print(f'  {row}')