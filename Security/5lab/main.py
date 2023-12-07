from os import system

from package.smm import SMM
from package.user import User
from package.shadow_reader import read_shadow_file


ADMIN_NAME = "rubybunny"

SL = SMM()
USERS = {user[0]: User(SL, user[1], 3 if user[0] == ADMIN_NAME else 1) for user in read_shadow_file()}


def login(username: str, password: str) -> User:
    try:
        user = USERS[username]
    except:
        raise Exception("User not found")

    if not user.compare_password(password):
        raise Exception("Wrong password")

    system("clear")
    return user


def main() -> None:
    system("clear")

    while True:
        username = input("Username: ")
        password = input("Password: ")

        user = login(username, password)

        while True:

            try:
                action = input("Action(r/w/e): ")

                match action:
                    case "r":
                        print(user.read_memory())
                    case "w":
                        index = int(input("Index: "))
                        value = int(input("Value: "))
                        user.modificate_memory(index, value)
                    case "e":
                        break
                    case _:
                        print("Wrong action")
            except Exception as e:
                print(e)

        system("clear")
        print("Exit")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        system("clear")
        print("Exit")
