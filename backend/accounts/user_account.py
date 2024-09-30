import logging
from typing import List, Optional, Dict
import datetime
import bcrypt
import re
from mutum_data_types import Custom_data

# Setup logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class InvalidEmailFormatError(Exception):
    """Custom exception raised when the email format is invalid."""
    pass

class InvalidDataFormatError(Exception):
    """Custom exception raised when data format is invalid."""
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

    # Password methods
    def set_password(self, password: str) -> None:
        salt = bcrypt.gensalt()
        self.__password_hash = bcrypt.hashpw(password.encode(), salt)
        logger.info("Password hash set successfully.")

    def check_password(self, password: str) -> bool:
        if self.__password_hash is None:
            logger.warning("No password has been set for this account.")
            return False
        return bcrypt.checkpw(password.encode(), self.__password_hash)

    # Email methods
    def add_email(self, email: str) -> bool:
        if not self.is_valid_email(email):
            logger.error("The email format is invalid: %s", email)
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
            logger.info(f"Email added successfully: {email_data.get_name()} - {email_data.format_data()}")
            return True
        except ValueError as ve:
            logger.exception("Failed to format email data: %s", email)
            raise InvalidDataFormatError("Failed to format email data.") from ve

    def is_valid_email(self, email: str) -> bool:
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def get_emails(self) -> List[str]:
        # Return the formatted data for each email
        return [email.get_custom_data() for email in self.__emails]

    # Government Document methods
    def add_gov_doc(self, name: str, format_counter: List[Dict[str, int]], size_wo_dividers: int, format_divider: Optional[List[Dict[str, str]]] = None, value: Optional[str] = None) -> bool:
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
            logger.info(f"Government document added successfully: {gov_doc.get_name()}")
            return True
        except ValueError as ve:
            logger.exception("Failed to format government document data: %s", name)
            raise InvalidDataFormatError("Failed to format government document data.") from ve

    def get_gov_docs(self) -> List[str]:
        return [doc.get_name() for doc in self.__gov_docs]

    # Phone Number methods
    def add_phone_number(self, name: str, format_counter: List[Dict[str, int]], size_wo_dividers: int, format_divider: Optional[List[Dict[str, str]]] = None, value: Optional[str] = None) -> bool:
        try:
            phone_number = Custom_data(
                name=name,
                format_counter=format_counter,
                size_wo_dividers=size_wo_dividers,
                format_divider=format_divider
            )
            if value:
                phone_number.set_value(value)  # Set the phone number value if provided
            self.__phone_numbers.append(phone_number)
            logger.info(f"Phone number added successfully: {phone_number.get_name()}")
            return True
        except ValueError as ve:
            logger.exception("Failed to format phone number data: %s", name)
            raise InvalidDataFormatError("Failed to format phone number data.") from ve

    def get_phone_numbers(self) -> List[str]:
        return [phone.get_name() for phone in self.__phone_numbers]

    # Address methods
    def add_address(self, name: str, format_counter: List[Dict[str, int]], size_wo_dividers: int, format_divider: Optional[List[Dict[str, str]]] = None, value: Optional[str] = None) -> bool:
        try:
            address = Custom_data(
                name=name,
                format_counter=format_counter,
                size_wo_dividers=size_wo_dividers,
                format_divider=format_divider
            )
            if value:
                address.set_value(value)  # Set the address value if provided
            self.__addresses.append(address)
            logger.info(f"Address added successfully: {address.get_name()}")
            return True
        except ValueError as ve:
            logger.exception("Failed to format address data: %s", name)
            raise InvalidDataFormatError("Failed to format address data.") from ve

    def get_addresses(self) -> List[str]:
        return [address.get_name() for address in self.__addresses]

    # Username methods
    def set_username(self, username: str) -> None:
        self.__username = username
        logger.info(f"Username set successfully: {username}")

    def get_username(self) -> Optional[str]:
        return self.__username

    # Birthday methods
    def set_birthday(self, date: datetime.date) -> None:
        if date > datetime.date.today():
            logger.error("Birthday cannot be set to a future date: %s", date)
            raise ValueError("Birthday cannot be in the future")
        self.__birthday = date
        logger.info(f"Birthday set successfully: {date}")

    def get_birthday(self) -> Optional[datetime.date]:
        return self.__birthday

    # Account creation time
    def get_time_of_creation(self) -> datetime.datetime:
        return self.__time_of_creation