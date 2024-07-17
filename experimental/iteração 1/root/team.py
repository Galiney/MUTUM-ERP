from typing import Type, List, Dict, Optional
import datetime, bcrypt, unittest

class Team:
  def __init__(self) -> None:
    self.__managers: List[Type[Employee]] = []
    self.__roles: List[Type[Role]] = []