from typing import Type, List, Dict
import datetime

from .money import Money

class Liability(Money):
    def __init__(self, value: float, code_name_country_number: str, obligation_acquisition_datetime: datetime) -> None:
        super().__init__(value, code_name_country_number)
        self.__obligation_acquisition_datetime: datetime = obligation_acquisition_datetime
        self.__expiration_datetime: datetime = None
        self.__interest_rate: float = None

    @property
    def obligation_acquisition_datetime(self) -> datetime:
        return self.__obligation_acquisition_datetime
    
    @obligation_acquisition_datetime.setter
    def obligation_acquisition_datetime(self, value: datetime) -> None:
        self.__obligation_acquisition_datetime = value

    @property
    def expiration_datetime(self) -> datetime:
        return self.__expiration_datetime
    
    @expiration_datetime.setter
    def expiration_datetime(self, value: datetime) -> None:
        self.__expiration_datetime = value

    @property
    def interest_rate(self) -> float:
        return self.__interest_rate
    
    @interest_rate.setter
    def interest_rate(self, value: float) -> None:
        self.__interest_rate = value
