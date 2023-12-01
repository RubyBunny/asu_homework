from sport_info import SportUser_namedTuple
from datetime import datetime, time
from custom_exceptions import *
from typing import List


def insert_user(data: List[SportUser_namedTuple], user: SportUser_namedTuple) -> List[SportUser_namedTuple]:
    if user in data:
        raise InsertionError
    else:
        data.append(user)
        return data


def delete_user(data: List, user) -> List:
    if user in data:
        return [item for item in data if item != user]
    else:
        raise DeletionError


if __name__ == "__main__":
    user = SportUser_namedTuple("surname", 3, "run", "coachsurname", datetime.fromisoformat(
        "2022-09-24 09:40:00"), time(0, 40), 100)
    second_user = SportUser_namedTuple("some", 2138, "jump", "coachsurname", datetime.fromisoformat(
        "2022-09-24 09:40:00"), time(0, 40), 100)
    data = [user, second_user]

    guest = SportUser_namedTuple("guest", 3217, "swiming", "coachsurname", datetime.fromisoformat(
        "2022-09-24 09:40:00"), time(0, 40), 100)
    data = insert_user(data, guest)
    print(data)

    data = delete_user(data, guest)
    print(data)
