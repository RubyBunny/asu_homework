from sport_info import SportUser_dataclass, SportUser_namedTuple, SportUser_typedDict
from datetime import datetime, time
from typing import List


def find_by_surname_in_dataclass(data: List[SportUser_dataclass], surname: str) -> List[SportUser_dataclass]:
    return [item for item in data if item.surname == surname]


def find_by_sportEvent_in_dataclass(data: List[SportUser_dataclass], sportEvent: str) -> List[SportUser_dataclass]:
    return [item for item in data if item.sportEvent == sportEvent]


def find_by_coachSurname_in_dataclass(data: List[SportUser_dataclass], coachSurname: str) -> List[SportUser_dataclass]:
    return [item for item in data if item.coachSurname == coachSurname]


def find_by_surname_in_namedtyple(data: List[SportUser_namedTuple], surname: str) -> List[SportUser_namedTuple]:
    return [item for item in data if item.surname == surname]


def find_by_sportEvent_in_namedtyple(data: List[SportUser_namedTuple], sportEvent: str) -> List[SportUser_namedTuple]:
    return [item for item in data if item.sportEvent == sportEvent]


def find_by_coachSurname_in_namedtyple(data: List[SportUser_namedTuple], coachSurname: str) -> List[SportUser_namedTuple]:
    return [item for item in data if item.coachSurname == coachSurname]


def find_by_surname_in_typeddict(data: List[SportUser_typedDict], surname: str) -> List[SportUser_typedDict]:
    return [item for item in data if item["surname"] == surname]


def find_by_sportEvent_in_typeddict(data: List[SportUser_typedDict], sportEvent: str) -> List[SportUser_typedDict]:
    return [item for item in data if item["sportEvent"] == sportEvent]


def find_by_coachSurname_in_typeddict(data: List[SportUser_typedDict], coachSurname: str) -> List[SportUser_typedDict]:
    return [item for item in data if item["coachSurname"] == coachSurname]


if __name__ == "__main__":
    user_namedTuple = SportUser_namedTuple(
        "surname", 3, "run", "coachsurname", datetime.fromisoformat("2022-09-24 09:40:00"), time(0, 40), 100)
