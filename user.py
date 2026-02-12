from datetime import datetime

class User:
    def __init__(self, user_id, name, surname, birthday, email=None, password=None):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.email = email
        self.password = password

    def get_details(self):
        return (f"ID: {self.user_id}\n"
                f"Name: {self.name} {self.surname}\n"
                f"Email: {self.email}\n"
                f"Birthday: {self.birthday.strftime('%Y-%m-%d')}")

    def get_age(self):
        today = datetime.today()
        age = today.year - self.birthday.year
        if (today.month, today.day) < (self.birthday.month, self.birthday.day):
            age -= 1
        return age
