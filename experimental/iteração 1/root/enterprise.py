from typing import Type, List, Dict, Optional
import datetime, bcrypt, unittest

class Enterprise:
    def __init__(self) -> None:
        self.__department_sectors: List[Type[Department_sector]] = []
        self.__roles: List[Type[Role]] = []
        self.__employees: List[Type[Employee]] = []
        self.__gov_docs: List[Custom_data] = []
        self.__assets: List[Type[Asset]] = []
        self.__liabilities: List[Type[Liability]] = []
        self.__expenses: List[Type[Expense]] = []
        self.__revenues: List[Type[Revenue]] = []

    def register_department_sector(self, department_sector: Type[Department_sector]) -> bool:
        try:
            self.__department_sectors.append(department_sector)
            return True
        except Exception as e:
            print(f"Error registering department/sector: {e}")
            return False

    def register_role(self, role: Type[Role]) -> bool:
        try:
            self.__roles.append(role)
            return True
        except Exception as e:
            print(f"Error registering role: {e}")
            return False

    def register_employee(self, employee: Type[Employee]) -> bool:
        try:
            self.__employees.append(employee)
            return True
        except Exception as e:
            print(f"Error registering employee: {e}")
            return False

    def add_government_document(self, document: Custom_data) -> bool: #! need to fix!
        try:
            self.__gov_docs.append(document)
            return True
        except Exception as e:
            print(f"Error adding government document: {e}")
            return False

    def add_asset(self, asset: Type[Asset]) -> bool:
        try:
            self.__assets.append(asset)
            return True
        except Exception as e:
            print(f"Error adding asset: {e}")
            return False

    def add_liability(self, liability: Type[Liability]) -> bool:
        try:
            self.__liabilities.append(liability)
            return True
        except Exception as e:
            print(f"Error adding liability: {e}")
            return False

    def add_expense(self, expense: Type[Expense]) -> bool:
        try:
            self.__expenses.append(expense)
            return True
        except Exception as e:
            print(f"Error adding expense: {e}")
            return False

    def add_revenue(self, revenue: Type[Revenue]) -> bool:
        try:
            self.__revenues.append(revenue)
            return True
        except Exception as e:
            print(f"Error adding revenue: {e}")
            return False