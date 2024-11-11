from . import *

class Team:
  def __init__(self) -> None:
    self.__managers: List[Employee] = []
    self.__roles: List[Role] = []