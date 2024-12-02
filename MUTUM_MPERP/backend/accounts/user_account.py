from typing import List, Optional, Dict, Type
import datetime
import re
<<<<<<< HEAD:MUTUM_MPERP/backend/accounts/user_account.py
from ..mutum_data_types import Custom_data
from ..enterprise import Enterprise
import copy
from .permissions import Permissions
#from logger import Logger  # Importando a classe Logger
=======
import bcrypt
from mutum_data_types import Custom_data
from .permissions import Permissions
#from ..mutum_logging import Logger
>>>>>>> bf3f5188e214c03e93141e591f941a302660265f:backend/accounts/user_account.py

class InvalidEmailFormatError(Exception):
    """Custom exception raised when the email format is invalid."""
    pass

class InvalidDataFormatError(Exception):
    """Custom exception raised when data format is invalid."""
    pass

class UnauthorizedActionError(Exception):
    """Custom exception raised when an action is not authorized."""
    pass

class User_account:
    def __init__(self, creator=None) -> None:
        self.__creator = creator if creator else self
        self.__emails: List[Custom_data] = []
        self.__gov_docs: List[Custom_data] = []
        self.__phone_numbers: List[Custom_data] = []
        self.__time_of_creation = datetime.datetime.now()
        self.__birthday: Optional[datetime.date] = None
        self.__addresses: List[Custom_data] = []
        self.__username: Optional[str] = None
        self.__password_hash: Optional[str] = None

        #system part
        self.__enterprises = []
        self.__permissions: Type[Permissions]
<<<<<<< HEAD:MUTUM_MPERP/backend/accounts/user_account.py
        #self.logger = Logger()  # Inicializando o Logger
        print("user criado")
=======
        #self.__apps: List[Apps]

        #self.logger = Logger() #inicializar aqui? 
>>>>>>> bf3f5188e214c03e93141e591f941a302660265f:backend/accounts/user_account.py

    # Authorization check
    def __is_creator(self):
        if self.__creator != self:
            #self.logger.warning("Unauthorized action attempt by non-creator.")
            raise UnauthorizedActionError("This action is only permitted by the account creator.")
        
    def check_permission(self, permission: str) -> bool:
        """Verifica se o usuário tem a permissão necessária."""
        if not self.permissions.check_permission(self.__role, permission):
            #self.logger.warning("Unauthorized action attempt: %s", permission)
            raise UnauthorizedActionError(f"Permission denied for action: {permission}")
        return True

    # Password methods
    def set_password(self, password: str) -> None:
        salt = bcrypt.gensalt()
        self.__password_hash = bcrypt.hashpw(password.encode(), salt)
<<<<<<< HEAD:MUTUM_MPERP/backend/accounts/user_account.py
        #self.logger.info("Password hash set successfully.")
=======
       # self.logger.info("Password hash set successfully.")
>>>>>>> bf3f5188e214c03e93141e591f941a302660265f:backend/accounts/user_account.py

    def check_password(self, password: str) -> bool:
        if self.__password_hash is None:
            #self.logger.warning("No password has been set for this account.")
            return False
        return bcrypt.checkpw(password.encode(), self.__password_hash)

    # Email methods
    def add_email(self, email: str) -> bool:
        self.check_permission("create_email")
        self.__is_creator()
        if not self.is_valid_email(email):
            #self.logger.error("The email format is invalid: %s", email)
            raise InvalidEmailFormatError("The email format is invalid according to RFC 5322 standards.")

        try:
            local, domain = email.split('@')
            format_counter = [
                {'name': 'local', 'length': len(local)},
                {'name': 'domain', 'length': len(domain)}
            ]
            format_divider = [{'name': 'Address Sign', 'divider': '@'}]

            email_data = Custom_data(
                name='email',
                format_counter=format_counter,
                size_wo_dividers=len(email) - 1,  # Correct size without dividers
                format_divider=format_divider
            )

            email_data.set_value(email)  # Set the email value
            self.__emails.append(email_data)
            #self.logger.info(f"Email added successfully: {email_data.get_name()} - {email_data.format_data()}")
            return True
        except ValueError as ve:
            #self.logger.exception("Failed to format email data: %s", email)
            raise InvalidDataFormatError("Failed to format email data.") from ve

    def remove_email(self, email: str) -> bool:
        """Remove an email if it exists, authorized by creator."""
        self.__is_creator()
        for email_data in self.__emails:
            if email_data.get_custom_data() == email:
                self.__emails.remove(email_data)
                #self.logger.info("Email removed successfully: %s", email)
                return True
        #self.logger.warning("Attempted to remove non-existent email: %s", email)
        return False

    def is_valid_email(self, email: str) -> bool:
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def get_emails(self) -> List[str]:
        return [email.get_custom_data() for email in self.__emails]

    # Government Document methods
    def add_gov_doc(self, name: str, format_counter: List[Dict[str, int]], size_wo_dividers: int, format_divider: Optional[List[Dict[str, str]]] = None, value: Optional[str] = None) -> bool:
        self.__is_creator()
        try:
            gov_doc = Custom_data(
                name=name,
                format_counter=format_counter,
                size_wo_dividers=size_wo_dividers,
                format_divider=format_divider
            )
            if value:
                gov_doc.set_value(value)  # Set the government document value if provided
            self.__gov_docs.append(gov_doc)
            #self.logger.info(f"Government document added successfully: {gov_doc.get_name()}")
            return True
        except ValueError as ve:
            #self.logger.exception("Failed to format government document data: %s", name)
            raise InvalidDataFormatError("Failed to format government document data.") from ve

    def remove_gov_doc(self, name: str) -> bool:
        """Remove a government document if it exists, authorized by creator."""
        self.__is_creator()
        for doc in self.__gov_docs:
            if doc.get_name() == name:
                self.__gov_docs.remove(doc)
                #self.logger.info("Government document removed successfully: %s", name)
                return True
        #self.logger.warning("Attempted to remove non-existent government document: %s", name)
        return False

    # Username methods
    def set_username(self, username: str) -> None:
        self.__is_creator()
        self.__username = username
        #self.logger.info(f"Username set successfully: {username}")

    def get_username(self) -> Optional[str]:
        return self.__username

    # Birthday methods
    def set_birthday(self, date: datetime.date) -> None:
        self.__is_creator()
        if date > datetime.date.today():
            #self.logger.error("Birthday cannot be set to a future date: %s", date)
            raise ValueError("Birthday cannot be in the future")
        self.__birthday = date
        #self.logger.info(f"Birthday set successfully: {date}")

    def get_birthday(self) -> Optional[datetime.date]:
        return self.__birthday

    # Account creation time
    def get_time_of_creation(self) -> datetime.datetime:
        return self.__time_of_creation
    
    def to_dict(self) -> dict:
        """Converte a instância para um dicionário serializável."""
        return {
            'emails': [email.get_custom_data() for email in self.__emails],
            'gov_docs': [doc.get_name() for doc in self.__gov_docs],
            'phone_numbers': [phone.get_custom_data() for phone in self.__phone_numbers],
            'time_of_creation': self.__time_of_creation.isoformat(),
            'birthday': self.__birthday.isoformat() if self.__birthday else None,
            'username': self.__username,
            'password_hash': self.__password_hash.decode() if self.__password_hash else None
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Cria uma instância de User_account a partir de um dicionário."""
        account = cls()
        account.__emails = [Custom_data(value=email) for email in data.get('emails', [])]
        account.__gov_docs = [Custom_data(name=doc) for doc in data.get('gov_docs', [])]
        account.__phone_numbers = [Custom_data(value=phone) for phone in data.get('phone_numbers', [])]
        account.__time_of_creation = datetime.datetime.fromisoformat(data['time_of_creation'])
        account.__birthday = datetime.date.fromisoformat(data['birthday']) if data['birthday'] else None
        account.__username = data.get('username')
        account.__password_hash = data['password_hash'].encode() if data.get('password_hash') else None
        return account