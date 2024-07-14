from root import *

class User_account:
    def __init__(self, creator=None) -> None:
        if creator is None:
            self.__creator = self  # Uma conta mutum, se for a primeira conta será a própria conta
        else:
            self.__creator = creator
        self.__emails: List[Type[Custom_data]] = {}
        self.__gov_docs: List[Custom_data] = {}
        self.__phone_numbers: List[Type[Custom_data]] = {}
        self.__date_of_creation: Type[datetime.date] = None
        self.__birthday: Type[datetime.date] = None
        self.__addresses: List[Type[Custom_data]] = {}
        self.__username: str = None
        self.__password_hash: str = None  # Armazenar o hash da senha

    def set_password(self, password: str) -> None:
        # Gera um salt e cria um hash seguro para a senha
        salt = bcrypt.gensalt()
        self.__password_hash = bcrypt.hashpw(password.encode(), salt)

    def check_password(self, password: str) -> bool:
        # Verifica se a senha fornecida corresponde ao hash armazenado
        if self.__password_hash is None:
            return False
        return bcrypt.checkpw(password.encode(), self.__password_hash)
