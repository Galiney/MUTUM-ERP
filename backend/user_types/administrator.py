from typing import List, Type

import importlib

from accounts import User_account
from enterprise import Enterprise, Department_sector, Team, Role

class Administrator(User_account):
    def __init__(self) -> None:
        super().__init__()  # Chama o construtor da classe pai
        self.__enterprises: List[Type[Enterprise]] = []

    def create_enterprise(self) -> bool:
        try:
            self.__enterprises.append(Enterprise())
            return True
        except Exception as e:
            print(f"Erro ao criar empresa: {e}")
            return False
    
    def create_department_sector(self, enterprise: Type[Enterprise]) -> bool:
        try:
            enterprise.register_department_sector(Department_sector())
            return True
        except Exception as e:
            print(f"Erro ao criar departamento/setor: {e}")
            return False

    def create_team(self, department_sector: Type[Department_sector]) -> bool:
        try:
            department_sector.create_team(Team())
            return True
        except Exception as e:
            print(f"Erro ao criar equipe: {e}")
            return False

    def create_role(self, enterprise: Type[Enterprise]) -> bool:
        try:
            enterprise.register_role(Role())
            return True
        except Exception as e:
            print(f"Erro ao criar função/role: {e}")
            return False

    def create_employee(self, enterprise: Type[Enterprise]) -> bool:
        try:
            employee_module = importlib.import_module('Employee')
            enterprise.register_employee(employee_module.Employee())
            return True
        except Exception as e:
            print(f"Erro ao criar funcionário: {e}")
            return False