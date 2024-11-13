from .money import Money

class Service:
    def __init__(self, name: str, description: str, hourly_rate: float, currency_code: str) -> None:
        self.__name: str = name
        self.__description: str = description
        self.__hourly_rate: Money = Money(hourly_rate, currency_code)

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description

    def get_hourly_rate(self) -> float:
        return self.__hourly_rate.get_value()

    def get_currency(self) -> str:
        return self.__hourly_rate.get_currency_code()

    def update_hourly_rate(self, new_rate: float) -> None:
        self.__hourly_rate = Money(new_rate, self.__hourly_rate.get_currency_code())
