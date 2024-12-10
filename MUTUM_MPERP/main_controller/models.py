from django.db import models
from django.contrib.auth.models import AbstractUser
from main_controller.backend.accounts.user_account import User_account
import datetime
from typing import List, Optional, Dict


class Accounts(AbstractUser):
    user_data = models.JSONField(
        null=False, blank=False,
        verbose_name="Dados do Usuário"
    )
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    password = models.CharField(max_length=128, default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")
    last_login = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'

    def save_user_account(self, user_account_instance: User_account):
        """
        Método para salvar os dados da classe User_account no modelo.
        """
        if isinstance(user_account_instance, User_account):
            self.user_data = user_account_instance.to_dict()  # Assume que a classe User_account tem um método to_dict()
            self.save()

    def __str__(self):
        return f"Account for {self.user_data.get('username', 'Unknown')}"

    # Métodos para acessar a classe User_account
    def get_user_account(self) -> User_account:
        """Retorna a instância de User_account associada a este modelo."""
        return User_account.from_dict(self.user_data)

    def add_email(self, email: str) -> bool:
        """Delegar para a classe User_account o método add_email."""
        user_account = self.get_user_account()
        return user_account.add_email(email)

    def remove_email(self, email: str) -> bool:
        """Delegar para a classe User_account o método remove_email."""
        user_account = self.get_user_account()
        return user_account.remove_email(email)

    def get_emails(self) -> List[str]:
        """Delegar para a classe User_account o método get_emails."""
        user_account = self.get_user_account()
        return user_account.get_emails()

    def set_username(self, username: str) -> None:
        """Delegar para a classe User_account o método set_username."""
        user_account = self.get_user_account()
        user_account.set_username(username)

    def get_username(self) -> Optional[str]:
        """Delegar para a classe User_account o método get_username."""
        user_account = self.get_user_account()
        return user_account.get_username()

    def set_birthday(self, date: datetime.date) -> None:
        """Delegar para a classe User_account o método set_birthday."""
        user_account = self.get_user_account()
        user_account.set_birthday(date)

    def get_birthday(self) -> Optional[datetime.date]:
        """Delegar para a classe User_account o método get_birthday."""
        user_account = self.get_user_account()
        return user_account.get_birthday()

    def set_password(self, password: str) -> None:
        """Delegar para a classe User_account o método set_password."""
        user_account = self.get_user_account()
        user_account.set_password(password)

    def check_password(self, password: str) -> bool:
        """Delegar para a classe User_account o método check_password."""
        user_account = self.get_user_account()
        return user_account.check_password(password)

    # Verificação de Permissões
    def check_permission(self, permission: str) -> bool:
        """Delegar para a classe User_account o método check_permission."""
        user_account = self.get_user_account()
        return user_account.check_permission(permission)

    # Métodos de documentos governamentais
    def add_gov_doc(self, name: str, format_counter: List[Dict[str, int]], size_wo_dividers: int, format_divider: Optional[List[Dict[str, str]]] = None, value: Optional[str] = None) -> bool:
        """Delegar para a classe User_account o método add_gov_doc."""
        user_account = self.get_user_account()
        return user_account.add_gov_doc(name, format_counter, size_wo_dividers, format_divider, value)

    def remove_gov_doc(self, name: str) -> bool:
        """Delegar para a classe User_account o método remove_gov_doc."""
        user_account = self.get_user_account()
        return user_account.remove_gov_doc(name)

    # Métodos de criação e obtenção de dados da conta
    def get_time_of_creation(self) -> datetime.datetime:
        """Retorna a data de criação da conta"""
        return self.created_at

    def to_dict(self) -> dict:
        """Converte os dados para um formato serializável"""
        return {
            'user_data': self.user_data,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
