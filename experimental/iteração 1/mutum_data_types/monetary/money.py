from mutum_data_types import *

class Money:
    def __init__(self, value: float, code_name_country_number: str) -> None:
        # Convert input to lowercase for case-insensitive search
        search_key = code_name_country_number.lower()

        # Initialize attributes with default values in case currency is not found
        self.__currency_name:str = None
        self.__currency_code:str = None
        self.__currency_country:str = None
        self.__currency_number:str = None
        self.__value:float = value

        # Check if the search key matches any currency info
        for code, currency in ISO_4217_ptbr.items():
            if (search_key == code.lower() or
                (currency.get("currency_name") and search_key == currency["currency_name"].lower()) or
                (currency.get("currency_country") and isinstance(currency["currency_country"], list) and
                 any(country and search_key == country.lower() for country in currency["currency_country"])) or
                (currency.get("currency_number") and search_key == currency["currency_number"].lower())):
                
                # Assign currency information if match is found
                self.__currency_name = currency["currency_name"]
                self.__currency_code = currency["currency_code"]
                self.__currency_country = currency["currency_country"]
                self.__currency_number = currency["currency_number"]
                break  # Stop searching after finding the first match

    def get_currency_name(self) -> str:
        return self.__currency_name
    
    def get_currency_code(self) -> str:
        return self.__currency_code
    
    def get_currency_country(self) -> List[str]:
        return self.__currency_country
    
    def get_currency_number(self) -> str:
        return self.__currency_number
    
    def get_value(self) -> float:
        return self.__value