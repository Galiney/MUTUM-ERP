import importlib
from typing import Type, List
from . import class_import_functions

# Carregar dinamicamente a classe User_account e usá-la como base para herança
User_account = class_import_functions['User_account']()

class Administrator(User_account):
    def __init__(self) -> None:
        super().__init__()  # Chama o construtor da classe pai
        self.__enterprises: List[Type[Enterprise]] = []

    def create_enterprise(self) -> bool:
        try:
            Enterprise = get_enterprise_class()
            self.__enterprises.append(Enterprise())
            return True
        except Exception as e:
            print(f"Erro ao criar empresa: {e}")
            return False
    
    def create_department_sector(self, enterprise: Type['Enterprise']) -> bool:
        try:
            Department_sector = get_department_sector_class()
            enterprise.register_department_sector(Department_sector())
            return True
        except Exception as e:
            print(f"Erro ao criar departamento/setor: {e}")
            return False

    def create_team(self, department_sector: Type['Department_sector']) -> bool:
        try:
            Team = get_team_class()
            department_sector.create_team(Team())
            return True
        except Exception as e:
            print(f"Erro ao criar equipe: {e}")
            return False

    def create_role(self, enterprise: Type['Enterprise']) -> bool:
        try:
            Role = get_role_class()
            enterprise.register_role(Role())
            return True
        except Exception as e:
            print(f"Erro ao criar função/role: {e}")
            return False

    def create_employee(self, enterprise: Type['Enterprise']) -> bool:
        try:
            Employee = get_employee_class()
            enterprise.register_employee(Employee())
            return True
        except Exception as e:
            print(f"Erro ao criar funcionário: {e}")
            return False
