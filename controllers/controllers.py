# -*- encoding:utf-8 -*-
from models.models import Models


class Controllers:
  def __init__(self) -> None:
    # Init singleton model
    Models()