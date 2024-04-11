# -*- encoding:utf-8 -*-
import toga
from views.GUI.pages.MainPage import MainPage
from views.GUI.pages.SettingsPage import SettingsPage
from views.GUI.utils.AbstractPage import Page


class TogaApp(toga.App):
  def startup(self):
    self.main_window = toga.MainWindow()
    self.current_page_container = toga.Box()

    # Create page instances
    self.pages = {
       'main': MainPage(app=self),
       'settings': SettingsPage(app=self)
    }

    # Set active page
    self.go_to_page('main')

    self.main_window.show()

  def go_to_page(self, page_name: str):
      # get the page wanted
      page: Page = self.pages.get(page_name)

      # replace the current page by the new one
      self.main_window.content = page.container