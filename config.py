# -*- encoding:utf-8 -*-
import os


global APP_PATH
global ENV
global STORAGE_BACKEND
APP_PATH = os.path.dirname(os.path.realpath(__file__))
ENV = 'dev'
STORAGE_BACKEND = 'file'  # 'file' to use TXT-based storage, 'sqlite' to use the database