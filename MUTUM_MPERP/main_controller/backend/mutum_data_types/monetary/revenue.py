from typing import Type, List, Dict
import datetime

from .money import Money

class Revenue(Money):
    def __init__(self, value: float, code_name_country_number: str, receipt_datetime: datetime) -> None:
        super().__init__(value, code_name_country_number)
        self.__receipt_datetime: datetime = receipt_datetime
        self.__income_datetime: datetime = None  # Initialize as None, set as needed
    
    def get_receipt_datetime(self) -> datetime:
        return self.__receipt_datetime
    
    def get_income_datetime(self) -> datetime:
        return self.__income_datetime
    
    def set_income_datetime(self, income_datetime: datetime) -> None:
        self.__income_datetime = income_datetime
