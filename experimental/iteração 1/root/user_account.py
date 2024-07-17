from typing import Type, List, Dict, Optional
import datetime, bcrypt, unittest

class User_account:
  def __init__(self, creator=None) -> None:
    if creator is None:
      self.__creator = self  # Uma conta mutuamente, se for a primeira conta será a própria conta
    else:
      self.__creator = creator
    self.__emails: List[Custom_data] = []
    self.__gov_docs: List[Custom_data] = []
    self.__phone_numbers: List[Custom_data] = []
    self.__time_of_creation: Optional[datetime.datetime] = None
    self.__birthday: Optional[datetime.date] = None
    self.__addresses: List[Custom_data] = []
    self.__username: Optional[str] = None
    self.__password_hash: Optional[str] = None  # Armazenar o hash da senha

  def set_password(self, password: str) -> None:
    # Gera um salt e cria um hash seguro para a senha
    salt = bcrypt.gensalt()
    self.__password_hash = bcrypt.hashpw(password.encode(), salt)

  def check_password(self, password: str) -> bool:
    # Verifica se a senha fornecida corresponde ao hash armazenado
    if self.__password_hash is None:
      return False
    return bcrypt.checkpw(password.encode(), self.__password_hash)

  def add_email(self, email: str) -> bool:
    try:
      local, domain = email.split('@')
      format_counter = [
        {'name': 'local', 'length': len(local)},
        {'name': 'domain', 'length': len(domain)}
      ]
      format_divider = [
        {'Adress Sign': '@'}
      ]
      email_data = Custom_data(
        name='email',
        format_counter=format_counter,
        size_wo_dividers=len(email) - 1,
        format_divider=format_divider
      )
      self.__emails.append(email_data)
      print(f"Email added: {email_data}")
      return True
    except ValueError:
      print("Invalid email address!")
      return False

  #! A ideia aqui é que a formatação seja resolvida no front
  def add_gov_doc(self, name: str, format_counter: List[Dict[str, int]], size_wo_dividers: int, format_divider: Optional[List[Dict[str, str]]] = None) -> bool:
    try:
      gov_doc = Custom_data(
        name=name,
        format_counter=format_counter,
        size_wo_dividers=size_wo_dividers,
        format_divider=format_divider
      )
      self.__gov_docs.append(gov_doc)
      print(f"Government document added: {gov_doc}")
      return True
    except ValueError:
      print("Invalid formatted information!")
      return False
  
  #! A ideia aqui é que a formatação seja resolvida no front
  def add_phone_number(self, name: str, format_counter: List[Dict[str, int]], size_wo_dividers: int, format_divider: Optional[List[Dict[str, str]]] = None) -> bool:
    try:
      phone_number = Custom_data(
        name=name,
        format_counter=format_counter,
        size_wo_dividers=size_wo_dividers,
        format_divider=format_divider
      )
      self.__phone_numbers.append(phone_number)
      print(f"Phone number added: {phone_number}")
      return True
    except ValueError:
      print("Invalid formatted information!")
      return False
  
  #! A ideia aqui é que a formatação seja resolvida no front
  def add_address(self, name: str, format_counter: List[Dict[str, int]], size_wo_dividers: int, format_divider: Optional[List[Dict[str, str]]] = None) -> bool:
    try:
      address = Custom_data(
        name=name,
        format_counter=format_counter,
        size_wo_dividers=size_wo_dividers,
        format_divider=format_divider
      )
      self.__addresses.append(address)
      print(f"Address added: {address}")
      return True
    except ValueError:
      print("Invalid formatted information!")
      return False
    
  def set_username(self, username: str) -> None:
    self.__username = username

  def set_birthday(self, date: datetime.date) -> None:
    self.__birthday = date