# -*- encoding:utf-8 -*-
import toga
from toga.style import Pack
from toga.constants import COLUMN
from controllers.ColorsCtrl import ColorsCtrl
from controllers.TemporalCtrl import TemporalCtrl
from views.GUI.utils.AbstractPage import AbstractPage


class MainPage(AbstractPage):
  def __init__(self, app):
    super().__init__(app)
    self.temporal_ctrl = TemporalCtrl()

    # test
    print('test colors query')
    self.colors_ctrl = ColorsCtrl()
    self.colors_ctrl.tests()

  def build(self) -> toga.Widget:
    self.label_title = toga.Label('Page principale', style=Pack(padding=(10,20,10), font_style='italic'))
    self.label_fest = toga.Label('Fête de ?', style=Pack(padding=(10,20,10)))
    self.display_fest_btn = toga.Button('Afficher la fête du jour', on_press=self.show_fest_callback, style=Pack(padding=(20,20,10)))
    self.go_to_settings_btn = toga.Button('Aller aux paramètres', on_press=self.go_to_settings_callback, style=Pack(padding=(10,20,20)))

    # Construct the UI
    container = toga.Box(children=[
      self.label_title,
      self.label_fest,
      self.display_fest_btn,
      self.go_to_settings_btn
    ], style=Pack(direction=COLUMN))
    
    return container

  # Function executed when btn is clicked
  def show_fest_callback(self, event=None):
    self.label_fest.text = self.temporal_ctrl.getFestName()
  
  def go_to_settings_callback(self, event=None):
    self._app.go_to_page('settings')