# -*- encoding:utf-8 -*-
from abc import ABC, abstractmethod
from toga import Widget
from typing import TypeVar


TypePage = TypeVar('TypePage', bound='AbstractPage')

"""
  Abstract class used to define base structure for class pages
  @abstractmethod is a decorator indicating that the function must be implemented in the child class
"""
class AbstractPage(ABC):
  def __init__(self, app) -> None:
    super().__init__()
    self._app = app  # __var indicates the property is protected (accessible only by children, not outside)
    self.container: Widget = self.build()

  # Method call to build the toga container of the page
  @abstractmethod
  def build(self) -> Widget:
    pass

  # Method call to destroy correctly the toga container of the page
  def destroy(self):
    self.container.remove()
    self.container = None

  def __del__(self):
    self.destroy()