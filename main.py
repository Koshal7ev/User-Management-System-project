from datetime import datetime
from user import User
from user_service import UserService
from user_util import UserUtil

user_id = UserUtil.generate_user_id()
password = UserUtil.generate_password()
email = UserUtil.generate_email("John", "Doe", "example.com")

user = User(user_id, "John", "Doe", datetime(2000, 1, 1), email, password)

UserService.add_user(user)

print(user.get_details())
print("Age:", user.get_age())
print("Total Users:", UserService.get_number())
