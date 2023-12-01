from sport_info import SportUser_dataclass, SportUser_namedTuple, SportUser_typedDict, TypeDict_from_dict, TypeDict_to_dict
from datetime import datetime, time
from typing import List
import json


# Named Tuple
def load_namedtuple_users(filepath: str) -> List[SportUser_namedTuple]:
    with open(filepath, "r") as file:
        data = json.load(file)

    return [SportUser_namedTuple.from_dict(item) for item in data]


def save_namedtuple_users(data: List[SportUser_namedTuple], filepath: str):
    data = [SportUser_namedTuple.to_dict(item) for item in data]

    with open(filepath, "w") as file:
        json.dump(data, file)


# Dataclass
def load_dataclass_users(filepath: str) -> List[SportUser_dataclass]:
    with open(filepath, "r") as file:
        data = json.load(file)

    return [SportUser_dataclass.from_dict(item) for item in data]


def save_dataclass_users(data: List[SportUser_dataclass], filepath: str):
    data = [SportUser_dataclass.to_dict(item) for item in data]

    with open(filepath, "w") as file:
        json.dump(data, file)


# Typed Dict
def load_typeddict_users(filepath: str) -> List[SportUser_typedDict]:
    with open(filepath, "r") as file:
        data = json.load(file)

    return [TypeDict_from_dict(item) for item in data]


def save_typeddict_users(data: List[SportUser_typedDict], filepath: str):
    data = [TypeDict_to_dict(item) for item in data]

    with open(filepath, "w") as file:
        json.dump(data, file)


def read_namedtuple_user_info() -> SportUser_namedTuple:
    surname = input("Enter surname: ")
    code = int(input("Enter code: "))
    sportEvent = input("Enter sport event: ")
    coachSurname = input("Enter coach surname: ")
    startDate = input("Enter start date: ")
    count = input("Enter count: ")
    priceForMinute = int(input("Enter price for minute: "))

    return SportUser_namedTuple(surname, code, sportEvent, coachSurname, startDate, count, priceForMinute)


def read_dataclass_user_info() -> SportUser_dataclass:
    surname = input("Enter surname: ")
    code = int(input("Enter code: "))
    sportEvent = input("Enter sport event: ")
    coachSurname = input("Enter coach surname: ")
    startDate = input("Enter start date: ")
    count = input("Enter count: ")
    priceForMinute = int(input("Enter price for minute: "))

    return SportUser_dataclass(surname, code, sportEvent, coachSurname, startDate, count, priceForMinute)


def read_typeddict_user_info() -> SportUser_typedDict:
    surname = input("Enter surname: ")
    code = int(input("Enter code: "))
    sportEvent = input("Enter sport event: ")
    coachSurname = input("Enter coach surname: ")
    startDate = input("Enter start date: ")
    count = input("Enter count: ")
    priceForMinute = int(input("Enter price for minute: "))

    return SportUser_typedDict(
        surname=surname,
        code=code,
        sportEvent=sportEvent,
        coachSurname=coachSurname,
        startDate=startDate,
        count=count,
        priceForMinute=priceForMinute
    )


if __name__ == "__main__":
    user_namedTuple = SportUser_namedTuple(
        "surname", 3, "run", "coachsurname", datetime.fromisoformat("2022-09-24 09:40:00"), time(0, 40), 100)
    save_namedtuple_users([user_namedTuple], "data.json")

    some_user = read_dataclass_user_info(SportUser_dataclass)
    print(some_user)
