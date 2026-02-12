+------------------+
|      User        |
+------------------+
| - user_id        |
| - name           |
| - surname        |
| - email          |
| - password       |
| - birthday       |
+------------------+
| + get_details()  |
| + get_age()      |
+------------------+

+------------------+
|   UserService    |
+------------------+
| + users (dict)   |
+------------------+
| + add_user()     |
| + find_user()    |
| + delete_user()  |
| + update_user()  |
| + get_number()   |
+------------------+

+------------------+
|    UserUtil      |
+------------------+
| + generate_user_id() |
| + generate_password()|
| + is_strong_password()|
| + generate_email()    |
| + validate_email()    |
+------------------+

# User Management System

## 📌 Project Description

This project is an object-oriented User Management System implemented in Python.

The system demonstrates:

- Instance variables and instance methods
- Class attributes and class methods
- Static methods
- Working with datetime
- Regular expressions (email validation)
- Unit testing
- Git version control

---

## 🧱 Project Structure

- user.py – User class implementation
- user_service.py – UserService class for managing users
- user_util.py – Utility class with static methods
- test_user.py – Unit tests for User class
- test_user_service.py – Unit tests for UserService
- test_user_util.py – Unit tests for UserUtil
- main.py – Example usage
- README.md – Project documentation

---

## 👤 User Class

Represents a single user.

Attributes:
- user_id
- name
- surname
- email
- password
- birthday

Methods:
- get_details()
- get_age()

---

## 🗂 UserService Class

Manages users using a dictionary.

Class attribute:
- users (stores all User objects)

Methods:
- add_user()
- find_user()
- delete_user()
- update_user()
- get_number()

---

## 🛠 UserUtil Class

Provides helper static methods:

- generate_user_id()
- generate_password()
- is_strong_password()
- generate_email()
- validate_email()

---

## ▶ How to Run

Run main file:

```bash
python main.py
