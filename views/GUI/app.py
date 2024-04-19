# -*- encoding:utf-8 -*-
from typing import Dict, Union
import toga
from views.GUI.pages.MainPage import MainPage
from views.GUI.pages.SettingsPage import SettingsPage

GenericPage = Union[MainPage, SettingsPage]


class TogaApp(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow()
        self.current_page_container = toga.Box()

        # Create page instances
        self.pages: Dict[str, MainPage | SettingsPage] = {
            "main": MainPage(app=self),
            "settings": SettingsPage(app=self),
        }

        # Set active page
        self.go_to_page("main")

        self.main_window.show()

    def go_to_page(self, page_name: str):
        # get the page wanted
        next_page = self.pages.get(page_name)
        if next_page is not None:
            self.page = next_page
        else:
            self.page = MainPage(app=self)

        # replace the current page by the new one
        self.main_window.content = self.page.container
