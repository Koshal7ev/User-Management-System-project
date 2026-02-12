import unittest
from datetime import datetime
from user import User

class TestUser(unittest.TestCase):

    def test_get_age(self):
        birthday = datetime(2000, 1, 1)
        user = User(1, "John", "Doe", birthday)
        self.assertTrue(user.get_age() >= 24)

    def test_get_details(self):
        birthday = datetime(2000, 1, 1)
        user = User(1, "John", "Doe", birthday)
        details = user.get_details()
        self.assertIn("John", details)

if __name__ == "__main__":
    unittest.main()
