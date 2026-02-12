import unittest
from user_util import UserUtil

class TestUserUtil(unittest.TestCase):

    def test_generate_user_id(self):
        user_id = UserUtil.generate_user_id()
        self.assertEqual(len(str(user_id)), 9)

    def test_generate_password(self):
        password = UserUtil.generate_password()
        self.assertTrue(UserUtil.is_strong_password(password))

    def test_generate_email(self):
        email = UserUtil.generate_email("John", "Doe", "example.com")
        self.assertEqual(email, "john.doe@example.com")

    def test_validate_email(self):
        self.assertTrue(UserUtil.validate_email("john.doe@example.com"))

if __name__ == "__main__":
    unittest.main()
