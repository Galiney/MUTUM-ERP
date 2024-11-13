from typing import Type, List

from entitys import Administrator, Employee
from .team import Team

class Department_sector:
  def __init__(self) -> None:
    self.__teams: List[Team] = []
    self.__roles: List[Role] = []
    self.__employees: List[Employee] = []