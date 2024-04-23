# -*- encoding:utf-8 -*-


"""
    Singleton pattern: https://refactoring.guru/fr/design-patterns/singleton/python/example
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
