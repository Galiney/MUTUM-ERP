from root import User_account, Custom_data, Expense, Role
from typing import List, Dict, Type

class Employee(User_account):
    def __init__(self, hiring_responsible: Type[User_account]) -> None:
        super().__init__(hiring_responsible)
        self.__hiring_responsible: Type[User_account] = hiring_responsible
        self.__hiring_gov_docs: List[Type[Custom_data]] = []
        self.__expenses: Dict[str, Type[Expense]] = {} #? Identificação aqui ou na classe?
        self.__roles: List[Role] = []

    def add_expense(self, expense_key: str, expense: Type[Expense]) -> None:
        self.__expenses[expense_key] = expense

    def add_role(self, role: Role) -> None:
        self.__roles.append(role)

    def get_hiring_responsible(self) -> Type[User_account]:
        return self.__hiring_responsible

    def get_hiring_gov_docs(self) -> List[Type[Custom_data]]:
        return self.__hiring_gov_docs

    def get_expenses(self) -> Dict[str, Type[Expense]]:
        return self.__expenses

    def get_roles(self) -> List[Role]:
        return self.__roles

    def set_hiring_gov_docs(self, gov_docs: List[Type[Custom_data]]) -> None:
        self.__hiring_gov_docs = gov_docs