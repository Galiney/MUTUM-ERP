from typing import Optional
from .money import Money

class Product:
    def __init__(self, name: str, description: str, price: float, currency_code: str) -> None:
        self.__name: str = name
        self.__description: str = description
        self.__price: Money = Money(price, currency_code)

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description

    def get_price(self) -> float:
        return self.__price.get_value()

    def get_currency(self) -> str:
        return self.__price.get_currency_code()

    def update_price(self, new_price: float) -> None:
        self.__price = Money(new_price, self.__price.get_currency_code())
