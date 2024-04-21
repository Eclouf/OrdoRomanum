# -*- encoding:utf-8 -*-
from typing import Protocol
import toga
from toga.style.pack import Pack
from toga.constants import COLUMN
import toga.widgets
import toga.widgets.button

from controllers.ControllerManager import ControllerManager
from views.GUI.utils.AbstractPage import AbstractPage


class MainPage(AbstractPage):
    def __init__(self, app):
        super().__init__(app)
        cm = ControllerManager
        self.temporal_ctrl = cm.get_temporal_ctrl()
        self.colors_ctrl = cm.get_colors_ctrl()
        self.occurence_ctrl = cm.get_occurrence_ctrl()
        self.contents_ctrl = cm.get_contents_ctrl()

        # For test 2 fests
        festA = {'title':'Fest of A','office':'office of A','rank':8500, 'occ':'F3U', 'con':'F1'}
        festB = {'title':'Fest of B','office':'office of B','rank':150, 'occ':'F2U', 'con':'jio2'}
        
        # test
        print("test colors query")
        self.colors_ctrl.tests()
        print("test occurence")
        self.occurence_ctrl.search(festA, festB)
        print("test contents")
        self.contents_ctrl.search(festA,festB)

    def build(self) -> toga.Widget:
        self.label_title = toga.Label(
            "Page principale", style=Pack(padding=(10, 20, 10), font_style="italic")
        )
        self.label_fest = toga.Label("Fête de ?", style=Pack(padding=(10, 20, 10)))
        self.display_fest_btn = toga.Button("Afficher la fête du jour", on_press=self.show_fest_callback, style=Pack(padding=(20, 20, 10)))  # type: ignore
        self.go_to_settings_btn = toga.Button("Aller aux paramètres", on_press=self.go_to_settings_callback, style=Pack(padding=(10, 20, 20)))  # type: ignore

        # Construct the UI
        container = toga.Box(
            children=[
                self.label_title,
                self.label_fest,
                self.display_fest_btn,
                self.go_to_settings_btn,
            ],
            style=Pack(direction=COLUMN),
        )

        return container

    # Function executed when btn is clicked
    def show_fest_callback(self, widget: toga.Button):
        self.label_fest.text = self.temporal_ctrl.get_fest_name()

    def go_to_settings_callback(self, widget: toga.Button):
        self._app.go_to_page("settings")
