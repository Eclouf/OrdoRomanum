# -*- encoding:utf-8 -*-
from abc import ABC, abstractmethod


"""
    AbstractDAO: provide attributes from ModelManager & interface to all DAOs
"""


class AbstractDAO(ABC):
    def __init__(self, model) -> None:
        super().__init__()
        self.session = model.session

    @abstractmethod
    def get_by_id(self):
        pass

    @abstractmethod
    def get_all(self):
        pass
