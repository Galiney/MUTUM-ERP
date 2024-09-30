from django.db import models
import logging
from typing import List
from .mutum_data_types import Custom_data  # Ajuste o caminho conforme necessário
from .user_account import User_account  # Ajuste o caminho conforme necessário

logger = logging.getLogger('myapp')

class UserAccountModel(models.Model):
    creator = models.CharField(max_length=255, null=True)  # Armazena o criador
    time_of_creation = models.DateTimeField(auto_now_add=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_account = User_account(creator=self.creator)

    # Métodos de interação com a classe User_account
    def set_password(self, password: str):
        self.user_account.set_password(password)
        logger.info("Password set in User_accountModel.")

    def check_password(self, password: str) -> bool:
        return self.user_account.check_password(password)

    def add_email(self, email: str) -> bool:
        return self.user_account.add_email(email)

    def get_emails(self) -> List[str]:
        return self.user_account.get_emails()

    def add_gov_doc(self, name: str, format_counter: List[Dict[str, int]], size_wo_dividers: int, format_divider: Optional[List[Dict[str, str]]] = None, value: Optional[str] = None) -> bool:
        return self.user_account.add_gov_doc(name, format_counter, size_wo_dividers, format_divider, value)

    def get_gov_docs(self) -> List[str]:
        return self.user_account.get_gov_docs()

    def add_phone_number(self, name: str, format_counter: List[Dict[str, int]], size_wo_dividers: int, format_divider: Optional[List[Dict[str, str]]] = None, value: Optional[str] = None) -> bool:
        return self.user_account.add_phone_number(name, format_counter, size_wo_dividers, format_divider, value)

    def get_phone_numbers(self) -> List[str]:
        return self.user_account.get_phone_numbers()

    def add_address(self, name: str, format_counter: List[Dict[str, int]], size_wo_dividers: int, format_divider: Optional[List[Dict[str, str]]] = None, value: Optional[str] = None) -> bool:
        return self.user_account.add_address(name, format_counter, size_wo_dividers, format_divider, value)

    def get_addresses(self) -> List[str]:
        return self.user_account.get_addresses()

    def set_username(self, username: str):
        self.user_account.set_username(username)

    def get_username(self) -> Optional[str]:
        return self.user_account.get_username()

    def set_birthday(self, date: datetime.date):
        self.user_account.set_birthday(date)

    def get_birthday(self) -> Optional[datetime.date]:
        return self.user_account.get_birthday()

    def get_time_of_creation(self) -> datetime.datetime:
        return self.user_account.get_time_of_creation()