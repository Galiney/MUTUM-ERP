from .role import Role
from typing import List

class Team:
  def __init__(self) -> None:
    self.__roles: List[Role] = []
    self.__employees = []