from typing import Optional
import datetime

class Pessoa:
    def __init__(self, nome: str, data_nascimento: datetime.date, email: Optional[str] = None, telefone: Optional[str] = None) -> None:
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__email = email
        self.__telefone = telefone

    # Métodos de acesso
    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str) -> None:
        self.__nome = nome

    def get_data_nascimento(self) -> datetime.date:
        return self.__data_nascimento

    def set_data_nascimento(self, data_nascimento: datetime.date) -> None:
        if data_nascimento > datetime.date.today():
            raise ValueError("A data de nascimento não pode ser no futuro.")
        self.__data_nascimento = data_nascimento

    def get_idade(self) -> int:
        """Calcula a idade da pessoa com base na data de nascimento."""
        hoje = datetime.date.today()
        idade = hoje.year - self.__data_nascimento.year
        if hoje.month < self.__data_nascimento.month or (hoje.month == self.__data_nascimento.month and hoje.day < self.__data_nascimento.day):
            idade -= 1
        return idade

    def get_email(self) -> Optional[str]:
        return self.__email

    def set_email(self, email: str) -> None:
        self.__email = email

    def get_telefone(self) -> Optional[str]:
        return self.__telefone

    def set_telefone(self, telefone: str) -> None:
        self.__telefone = telefone

    def __str__(self) -> str:
        return f"Nome: {self.__nome}, Data de Nascimento: {self.__data_nascimento}, Email: {self.__email}, Telefone: {self.__telefone}"
