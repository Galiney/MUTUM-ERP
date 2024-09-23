from typing import Type, List, Dict
import datetime

from .money import Money

class Asset(Money):
    def __init__(self, value: float, code_name_country_number: str, acquisition_datetime: datetime) -> None:
        super().__init__(value, code_name_country_number)
        self.__acquisition_datetime: datetime = acquisition_datetime
        self.__lifespan: datetime = None
    
    @property
    def acquisition_datetime(self) -> datetime:
        return self.__acquisition_datetime
    
    @acquisition_datetime.setter
    def acquisition_datetime(self, acquisition_datetime: datetime) -> None:
        self.__acquisition_datetime = acquisition_datetime
    
    @property
    def lifespan(self) -> datetime:
        return self.__lifespan
    
    @lifespan.setter
    def lifespan(self, lifespan: datetime) -> None:
        self.__lifespan = lifespan
