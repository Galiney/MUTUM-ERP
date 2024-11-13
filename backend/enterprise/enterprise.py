from typing import List
from entitys import Employee
from mutum_data_types import Expense, Revenue, Asset, Liability, Custom_data
from .department_sector import Department_sector
from .role import Role
import logging

logging.basicConfig(level=logging.ERROR)

class Enterprise:
    def __init__(self) -> None:
        
        self.__department_sectors: List[Department_sector] = []
        self.__teams: List[Team] = []
        self.__roles: List[Role] = []
        self.__employees: List[Employee] = []
        self.__gov_docs: List[Custom_data] = []
        self.__assets: List[Asset] = []
        self.__liabilities: List[Liability] = []
        self.__expenses: List[Expense] = []
        self.__revenues: List[Revenue] = []

    def register_department_sector(self, department_sector: Department_sector) -> bool:
        try:
            self.__department_sectors.append(department_sector)
            return True
        except Exception as e:
            logging.error(f"Error registering department/sector: {e}")
            return False

    def register_role(self, role: Role) -> bool:
        try:
            self.__roles.append(role)
            return True
        except Exception as e:
            logging.error(f"Error registering role: {e}")
            return False

    def register_employee(self, employee: Employee) -> bool:
        try:
            self.__employees.append(employee)
            return True
        except Exception as e:
            logging.error(f"Error registering employee: {e}")
            return False

    def add_government_document(self, document: Custom_data) -> bool:
        try:
            self.__gov_docs.append(document)
            return True
        except Exception as e:
            logging.error(f"Error adding government document: {e}")
            return False

    def add_asset(self, asset: Asset) -> bool:
        try:
            self.__assets.append(asset)
            return True
        except Exception as e:
            logging.error(f"Error adding asset: {e}")
            return False

    def add_liability(self, liability: Liability) -> bool:
        try:
            self.__liabilities.append(liability)
            return True
        except Exception as e:
            logging.error(f"Error adding liability: {e}")
            return False

    def add_expense(self, expense: Expense) -> bool:
        try:
            self.__expenses.append(expense)
            return True
        except Exception as e:
            logging.error(f"Error adding expense: {e}")
            return False

    def add_revenue(self, revenue: Revenue) -> bool:
        try:
            self.__revenues.append(revenue)
            return True
        except Exception as e:
            logging.error(f"Error adding revenue: {e}")
            return False
