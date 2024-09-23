import unittest
from datetime import datetime, date
from mutum_data_types import Custom_data
from accounts import User_account, InvalidEmailFormatError

class TestUserAccount(unittest.TestCase):
    
    def setUp(self):
        self.user = User_account()
    
    def test_set_password(self):
        self.user.set_password("securePassword123")
        self.assertTrue(self.user.check_password("securePassword123"))
        self.assertFalse(self.user.check_password("wrongPassword"))

    def test_add_valid_email(self):
        result = self.user.add_email("test@example.com")
        self.assertTrue(result)
        self.assertIn("test@example.com", self.user.get_emails())

    def test_add_invalid_email(self):
        with self.assertRaises(InvalidEmailFormatError):
            self.user.add_email("invalid-email-format")

    def test_add_government_document(self):
        result = self.user.add_gov_doc("Passport", [{'name': 'number', 'length': 9}], 9)
        self.assertTrue(result)
        self.assertIn("Passport", self.user.get_gov_docs())

    def test_add_phone_number(self):
        result = self.user.add_phone_number("123-456-7890", [{'name': 'digits', 'length': 10}], 10)
        self.assertTrue(result)
        self.assertIn("123-456-7890", self.user.get_phone_numbers())

    def test_add_address(self):
        result = self.user.add_address("123 Main St", [{'name': 'street', 'length': 12}], 12)
        self.assertTrue(result)
        self.assertIn("123 Main St", self.user.get_addresses())

    def test_set_username(self):
        self.user.set_username("testuser")
        self.assertEqual(self.user.get_username(), "testuser")

    def test_set_birthday(self):
        self.user.set_birthday(date(2000, 1, 1))
        self.assertEqual(self.user.get_birthday(), date(2000, 1, 1))

    def test_set_birthday_future(self):
        future_date = date.today().replace(year=date.today().year + 1)
        with self.assertRaises(ValueError):
            self.user.set_birthday(future_date)

    def test_get_time_of_creation(self):
        creation_time = self.user.get_time_of_creation()
        self.assertIsInstance(creation_time, datetime)

if __name__ == "__main__":
    unittest.main()