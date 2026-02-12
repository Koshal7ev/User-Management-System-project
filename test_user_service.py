import unittest
from datetime import datetime
from user import User
from user_service import UserService

class TestUserService(unittest.TestCase):

    def test_add_and_find_user(self):
        user = User(1, "Jane", "Doe", datetime(1999, 5, 5))
        UserService.add_user(user)
        self.assertIsNotNone(UserService.find_user(1))

    def test_delete_user(self):
        user = User(2, "Mark", "Smith", datetime(1998, 3, 3))
        UserService.add_user(user)
        self.assertTrue(UserService.delete_user(2))

if __name__ == "__main__":
    unittest.main()
