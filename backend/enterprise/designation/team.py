from . import *

class Team:
  def __init__(self) -> None:
    self.__roles: List[Role] = []
    self.__employees: List[Employee] = []