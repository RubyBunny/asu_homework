from package.smm import SMM
from package.user import User
from package.shadow_reader import read_shadow_file


SL = SMM()
USERS = {user[0]: User(SL, user[1]) for user in read_shadow_file()}


def main() -> None:
    username = input("Username: ")
    password = input("Password: ")

    try:
        user = USERS[username]
    except:
        raise Exception("User not found")

    if not user.compare_password(password):
        raise Exception("Wrong password")

    while True:
        action = input("Action(r/w/c/e): ")

        match action:
            case "r":
                print(user.read_memory())
            case "w":
                index = int(input("Index: "))
                value = int(input("Value: "))
                user.modificate_memory(index, value)
            case "c":
                permissions = int(input("Permissions: "))
                user.chmod(permissions)
            case "e":
                break
            case _:
                print("Wrong action")

    print("Exit")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        print("Exit")
