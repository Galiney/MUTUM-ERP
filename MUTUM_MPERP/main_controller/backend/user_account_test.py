import unittest
import datetime
from unittest.mock import MagicMock
from datetime import date
from mutum_data_types import Custom_data
from enterprise import Enterprise
from accounts import *

class TestUserAccount(unittest.TestCase):
    def setUp(self):
        # Criação de uma instância da classe para teste
        self.user_account = User_account()
        self.mock_email_data = MagicMock(spec=Custom_data)
        self.mock_permission = MagicMock(spec=Permissions)
        self.mock_enterprise = MagicMock(spec=Enterprise)

    # Testes de senha
    def test_set_and_check_password(self):
        self.user_account.set_password("secure_password")
        self.assertTrue(self.user_account.check_password("secure_password"))
        self.assertFalse(self.user_account.check_password("wrong_password"))

    # Testes de email
    def test_add_valid_email(self):
        valid_email = "test@example.com"
        self.user_account.add_email(valid_email)
        self.assertIn(valid_email, self.user_account.get_emails())

    def test_add_invalid_email(self):
        invalid_email = "invalid_email.com"
        with self.assertRaises(InvalidEmailFormatError):
            self.user_account.add_email(invalid_email)

    def test_remove_email(self):
        email = "test@example.com"
        self.user_account.add_email(email)
        result = self.user_account.remove_email(email)
        self.assertTrue(result)
        self.assertNotIn(email, self.user_account.get_emails())

    def test_remove_non_existent_email(self):
        email = "non_existent@example.com"
        result = self.user_account.remove_email(email)
        self.assertFalse(result)

    # Testes de username
    def test_set_and_get_username(self):
        username = "test_user"
        self.user_account.set_username(username)
        self.assertEqual(self.user_account.get_username(), username)

    # Testes de aniversário
    def test_set_and_get_birthday(self):
        valid_date = date(2000, 1, 1)
        self.user_account.set_birthday(valid_date)
        self.assertEqual(self.user_account.get_birthday(), valid_date)

    def test_set_birthday_in_future(self):
        future_date = date.today().replace(year=date.today().year + 1)
        with self.assertRaises(ValueError):
            self.user_account.set_birthday(future_date)

    # Teste de documentos governamentais
    def test_add_and_remove_gov_doc(self):
        name = "CPF"
        format_counter = [{"name": "digit", "length": 11}]
        size_wo_dividers = 11
        gov_doc_value = "12345678901"

        self.user_account.add_gov_doc(name, format_counter, size_wo_dividers, value=gov_doc_value)
        gov_docs = [doc.get_name() for doc in self.user_account._User_account__gov_docs]
        self.assertIn(name, gov_docs)

        self.user_account.remove_gov_doc(name)
        gov_docs = [doc.get_name() for doc in self.user_account._User_account__gov_docs]
        self.assertNotIn(name, gov_docs)

    # Testes de data de criação
    def test_get_time_of_creation(self):
        creation_time = self.user_account.get_time_of_creation()
        self.assertIsInstance(creation_time, datetime.datetime)

if __name__ == "__main__":
    unittest.main()
