from typing import Type, List

from entitys import Administrator, Employee
from .team import Team

class Department_sector:
  def __init__(self) -> None:
    self.__leaders: List[Type[Administrator]] = []
    self.__teams: List[Type[Team]] = []

  def assign_leader(self, employee: Type[Employee]) -> bool:
    try:
      self.__leaders.append(employee)
      return True
    except Exception as e:
      print(f"Erro ao designar líder: {e}")
      return False
  
  def create_team(self) -> bool:
    try:
      self.__teams.append(Team())
      return True
    except Exception as e:
      print(f"Erro ao registrar equipe: {e}")
      return False