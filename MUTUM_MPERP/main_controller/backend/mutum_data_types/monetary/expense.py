from typing import Type, List, Dict
import datetime

from .liability import Liability

class Expense(Liability):
    def __init__(self, value: float, code_name_country_number: str, incurrence_datetime: datetime) -> None:
        super().__init__(value, code_name_country_number, incurrence_datetime)
        self.__incurrence_datetime: datetime = incurrence_datetime
        self.__payment_datetime: datetime = None
    
    @property
    def incurrence_datetime(self) -> datetime:
        return self.__incurrence_datetime
    
    @incurrence_datetime.setter
    def incurrence_datetime(self, incurrence_datetime: datetime) -> None:
        self.__incurrence_datetime = incurrence_datetime
    
    @property
    def payment_datetime(self) -> datetime:
        return self.__payment_datetime
    
    @payment_datetime.setter
    def payment_datetime(self, payment_datetime: datetime) -> None:
        self.__payment_datetime = payment_datetime
