from typing import Type, List, Dict, Optional
import datetime, bcrypt, unittest

class Role:
  def __init__(self) -> None:
    self.__employess: List[Type[Employee]] = []