from sport_info import *

def format_sport_info(sportUser:  SportUser_dataclass or SportUser_namedTuple) -> str:
    return (f"\nФамилия клиента: {sportUser.surname}\n"
            f"Код: {sportUser.code}\n"
            f"Вид спортивного занятия: {sportUser.sportEvent}\n"
            f"Фамилия тренера: {sportUser.coachSurname}\n"
            f"Дата и время начала: {sportUser.startDate}\n"
            f"Количество минут: {sportUser.count}\n"
            f"Тариф за минуту: {sportUser.priceForMinute}")

def format_sport_info_typedDict(sportUser: SportUser_typedDict) -> str:
    return (f"\nФамилия клиента: {sportUser['surname']}\n"
            f"Код: {sportUser['code']}\n"
            f"Вид спортивного занятия: {sportUser['sportEvent']}\n"
            f"Фамилия тренера: {sportUser['coachSurname']}\n"
            f"Дата и время начала: {sportUser['startDate']}\n"
            f"Количество минут: {sportUser['count']}\n"
            f"Тариф за минуту: {sportUser['priceForMinute']}")

if __name__ == "__main__":
    user_dataclass = SportUser_dataclass("surname", 3, "run", "coachsurname", datetime.fromisoformat("2022-09-24 09:40:00"), time(0, 40), 100)
    user_namedTuple = SportUser_namedTuple("surname", 3, "run", "coachsurname", datetime.fromisoformat("2022-09-24 09:40:00"), time(0, 40), 100)
    user_typedDict = SportUser_typedDict(
        surname="surname", 
        code=3, 
        sportEvent="run", 
        coachSurname="coachsurname", 
        startDate=datetime.fromisoformat("2022-09-24 09:40:00"), 
        count=time(0, 40), 
        priceForMinute=100
    )

    print(format_sport_info(user_dataclass))
    print(format_sport_info(user_namedTuple))
    print(format_sport_info_typedDict(user_typedDict))