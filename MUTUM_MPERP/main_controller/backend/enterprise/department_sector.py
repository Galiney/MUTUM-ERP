from typing import Type, List

from .designation import Team, Role

class Department_sector:
  def __init__(self) -> None:
    self.__teams: List[Team] = []
    self.__roles: List[Role] = []
    self.__employees = []

