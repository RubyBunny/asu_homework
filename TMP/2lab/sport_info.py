from typing import NamedTuple, TypedDict
from datetime import datetime, time
from dataclasses import dataclass


@dataclass
class SportUser_dataclass:
    surname: str
    code: int
    sportEvent: str
    coachSurname: str
    startDate: datetime
    count: time
    priceForMinute: int

    def to_dict(self) -> dict:
        return {
            "surname": self.surname,
            "code": self.code,
            "sportEvent": self.sportEvent,
            "coachSurname": self.coachSurname,
            "startDate": str(self.startDate),
            "count": str(self.count),
            "priceForMinute": self.priceForMinute
        }

    @classmethod
    def from_dict(cls, data):
        return SportUser_dataclass(
            data["surname"],
            data["code"],
            data["sportEvent"],
            data["coachSurname"],
            data["startDate"],
            data["count"],
            data["priceForMinute"]
        )


class SportUser_namedTuple(NamedTuple):
    surname: str
    code: int
    sportEvent: str
    coachSurname: str
    startDate: datetime
    count: time
    priceForMinute: int

    def to_dict(self) -> dict:
        return {
            "surname": self.surname,
            "code": self.code,
            "sportEvent": self.sportEvent,
            "coachSurname": self.coachSurname,
            "startDate": str(self.startDate),
            "count": str(self.count),
            "priceForMinute": self.priceForMinute
        }

    @classmethod
    def from_dict(cls, data):
        return SportUser_namedTuple(
            data["surname"],
            data["code"],
            data["sportEvent"],
            data["coachSurname"],
            data["startDate"],
            data["count"],
            data["priceForMinute"]
        )


class SportUser_typedDict(TypedDict):
    surname: str
    code: int
    sportEvent: str
    coachSurname: str
    startDate: datetime
    count: time
    priceForMinute: int


def TypeDict_to_dict(data: SportUser_typedDict) -> dict:
    return {
        "surname": data["surname"],
        "code": data["code"],
        "sportEvent": data["sportEvent"],
        "coachSurname": data["coachSurname"],
        "startDate": str(data["startDate"]),
        "count": str(data["count"]),
        "priceForMinute": data["priceForMinute"]
    }


def TypeDict_from_dict(data) -> SportUser_typedDict:
    return SportUser_typedDict(
        surname=data["surname"],
        code=data["code"],
        sportEvent=data["sportEvent"],
        coachSurname=data["coachSurname"],
        startDate=data["startDate"],
        count=data["count"],
        priceForMinute=data["priceForMinute"]
    )


if __name__ == "__main__":
    user_dataclass = SportUser_dataclass("surname", 3, "run", "coachsurname", datetime.fromisoformat(
        "2022-09-24 09:40:00"), time(0, 40), 100)
    user_namedTuple = SportUser_namedTuple(
        "surname", 3, "run", "coachsurname", datetime.fromisoformat("2022-09-24 09:40:00"), time(0, 40), 100)
    user_typedDict = SportUser_typedDict(
        surname="surname",
        code=3,
        sportEvent="run",
        coachSurname="coachsurname",
        startDate=datetime.fromisoformat("2022-09-24 09:40:00"),
        count=time(0, 40),
        priceForMinute=100
    )

    print(user_dataclass.to_dict())
    print(user_namedTuple.to_dict())
    print(TypeDict_to_dict(user_typedDict))
