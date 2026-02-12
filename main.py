from datetime import datetime
from user import User
from user_service import UserService
from user_util import UserUtil


def create_user():
    print("\n=== Создание пользователя ===")

    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    birthday_input = input("Введите дату рождения (YYYY-MM-DD): ")
    domain = input("Введите домен для email (например gmail.com): ")

    try:
        birthday = datetime.strptime(birthday_input, "%Y-%m-%d")
    except ValueError:
        print("❌ Неверный формат даты!")
        return

    user_id = UserUtil.generate_user_id()
    password = UserUtil.generate_password()
    email = UserUtil.generate_email(name, surname, domain)

    user = User(user_id, name, surname, birthday, email, password)
    UserService.add_user(user)

    print("\n✅ Пользователь создан!")
    print(user.get_details())
    print("Пароль:", password)


def find_user():
    print("\n=== Поиск пользователя ===")
    try:
        user_id = int(input("Введите ID пользователя: "))
    except ValueError:
        print("❌ ID должен быть числом!")
        return

    user = UserService.find_user(user_id)

    if user:
        print("\n✅ Пользователь найден:")
        print(user.get_details())
        print("Возраст:", user.get_age())
    else:
        print("❌ Пользователь не найден!")


def delete_user():
    print("\n=== Удаление пользователя ===")
    try:
        user_id = int(input("Введите ID пользователя: "))
    except ValueError:
        print("❌ ID должен быть числом!")
        return

    if UserService.delete_user(user_id):
        print("✅ Пользователь удалён!")
    else:
        print("❌ Пользователь не найден!")


def show_count():
    print("\nВсего пользователей:", UserService.get_number())


def menu():
    while True:
        print("\n===== USER MANAGEMENT SYSTEM =====")
        print("1. Создать пользователя")
        print("2. Найти пользователя")
        print("3. Удалить пользователя")
        print("4. Количество пользователей")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            find_user()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            show_count()
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("❌ Неверный выбор!")


if __name__ == "__main__":
    menu()
