from root import *

class TestUserAccount(unittest.TestCase):
    def setUp(self):
        self.user1 = User_account()

    def test_set_password(self):
        self.user1.set_password("senha123")
        self.assertIsNotNone(self.user1._User_account__password_hash)

    def test_check_password(self):
        self.user1.set_password("senha123")
        self.assertTrue(self.user1.check_password('senha123'))
        self.assertFalse(self.user1.check_password('senha456'))

    def test_add_email(self):
        self.assertTrue(self.user1.add_email("user@example.com"))
        self.assertFalse(self.user1.add_email("invalid_email"))

    def test_add_gov_doc(self):
        self.assertTrue(self.user1.add_gov_doc("Document 1", [{'part1': 5}, {'part2': 10}], 15, [{'Divider Sign': '-'}]))

    def test_add_phone_number(self):
        self.assertTrue(self.user1.add_phone_number("Phone 1", [{'part1': 3}, {'part2': 7}], 10, [{'Divider Sign': '-'}]))

    def test_add_address(self):
        self.assertTrue(self.user1.add_address("Address 1", [{'part1': 2}, {'part2': 8}], 10, [{'Divider Sign': ','}]))

    def test_set_username(self):
        self.user1.set_username("user123")
        self.assertEqual(self.user1._User_account__username, "user123")

    def test_set_birthday(self):
        test_date = date(1990, 5, 15)
        self.user1.set_birthday(test_date)
        self.assertEqual(self.user1._User_account__birthday, test_date)

if __name__ == "__main__":
    unittest.main()