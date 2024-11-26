from typing import List
from .team import Team
from .role import Role

class Department_sector:
    def __init__(self) -> None:
        self.__teams: List[Team] = []
        self.__roles: List[Role] = []
        self.__employees = []
