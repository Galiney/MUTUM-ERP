<<<<<<< HEAD:MUTUM_MPERP/backend/enterprise/department_sector.py
from typing import Type, List

from .designation import Team, Role

class Department_sector:
  def __init__(self) -> None:
    self.__teams: List[Team] = []
    self.__roles: List[Role] = []
    self.__employees = []
=======
from typing import List
from .team import Team
from .role import Role

class Department_sector:
    def __init__(self) -> None:
        self.__teams: List[Team] = []
        self.__roles: List[Role] = []
        self.__employees = []
>>>>>>> bf3f5188e214c03e93141e591f941a302660265f:backend/enterprise/department_sector.py
