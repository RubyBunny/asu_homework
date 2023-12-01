import argparse
from sport_io import *
from sport_info import *
from sport_find import *
from sport_formatter import *
from sport_insert_delete import *


def main():
    parser = argparse.ArgumentParser()

    typing_group = parser.add_mutually_exclusive_group()
    typing_group.add_argument("-nt", "--namedtuple",
                              type=bool, action=argparse.BooleanOptionalAction)
    typing_group.add_argument("-dt", "--dataclass",
                              type=bool, action=argparse.BooleanOptionalAction)
    typing_group.add_argument("-td", "--typeddict",
                              type=bool, action=argparse.BooleanOptionalAction)

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--create", type=str,
                       help="create empty data file")
    group.add_argument("-i", "--insert", type=str, help="insert data")
    group.add_argument("-d", "--delete", type=str, help="delete data")
    group.add_argument("-fn", "--findsurname", type=str,
                       help="find user by surname")
    group.add_argument("-fs", "--findsport", type=str,
                       help="find user by sport event")
    group.add_argument("-fc", "--findcoach", type=str,
                       help="find user by coach surname")
    group.add_argument("-p", "--print", type=str, help="print data")
    args = parser.parse_args()

    if args.create:
        if args.namedtuple:
            save_namedtuple_users([], args.create)
        elif args.dataclass:
            save_dataclass_users([], args.create)
        else:
            save_typeddict_users([], args.create)

    elif args.insert:
        if args.namedtuple:
            data = load_namedtuple_users(args.insert)
            inserted_user = read_namedtuple_user_info()
            try:
                data = insert_user(data, inserted_user)
            except InsertionError:
                print('Inserting something wrong!')
            finally:
                save_namedtuple_users(data, args.insert)

        elif args.dataclass:
            data = load_dataclass_users(args.insert)
            inserted_user = read_dataclass_user_info()
            try:
                data = insert_user(data, inserted_user)
            except InsertionError:
                print('Inserting something wrong!')
            finally:
                save_dataclass_users(data, args.insert)

        else:
            data = load_typeddict_users(args.insert)
            inserted_user = read_typeddict_user_info()
            try:
                data = insert_user(data, inserted_user)
            except InsertionError:
                print('Inserting something wrong!')
            finally:
                save_typeddict_users(data, args.insert)

    elif args.delete:
        if args.namedtuple:
            data = load_namedtuple_users(args.delete)
            deleted_user = read_namedtuple_user_info()
            try:
                data = delete_user(data, deleted_user)
            except InsertionError:
                print('Inserting something wrong!')
            finally:
                save_namedtuple_users(data, args.delete)

        elif args.dataclass:
            data = load_dataclass_users(args.delete)
            deleted_user = read_dataclass_user_info()
            try:
                data = delete_user(data, deleted_user)
            except InsertionError:
                print('Inserting something wrong!')
            finally:
                save_dataclass_users(data, args.delete)

        else:
            data = load_typeddict_users(args.delete)
            deleted_user = read_typeddict_user_info()
            try:
                data = delete_user(data, deleted_user)
            except InsertionError:
                print('Inserting something wrong!')
            finally:
                save_typeddict_users(data, args.delete)

    elif args.findsurname:
        if args.namedtuple:
            data = load_namedtuple_users(args.findsurname)
            surname = input('Surname to find: ')
            results = find_by_surname_in_namedtyple(data, surname)
            if results:
                for item in results:
                    print(format_sport_info(item))
            else:
                print('No users with this surname!')

        elif args.dataclass:
            data = load_dataclass_users(args.findsurname)
            surname = input('Surname to find: ')
            results = find_by_surname_in_dataclass(data, surname)
            if results:
                for item in results:
                    print(format_sport_info(item))
            else:
                print('No users with this surname!')

        else:
            data = load_typeddict_users(args.findsurname)
            surname = input('Surname to find: ')
            results = find_by_surname_in_typeddict(data, surname)
            if results:
                for item in results:
                    print(format_sport_info_typedDict(item))
            else:
                print('No users with this surname!')

    elif args.findsport:
        if args.namedtuple:
            data = load_namedtuple_users(args.findsport)
            sport = input('Sport to find: ')
            results = find_by_sportEvent_in_namedtyple(data, sport)
            if results:
                for item in results:
                    print(format_sport_info(item))
            else:
                print('No users with this sport event!')

        elif args.dataclass:
            data = load_dataclass_users(args.findsport)
            sport = input('Sport to find: ')
            results = find_by_sportEvent_in_dataclass(data, sport)
            if results:
                for item in results:
                    print(format_sport_info(item))
            else:
                print('No users with this sport event!')

        else:
            data = load_typeddict_users(args.findsport)
            sport = input('Sport to find: ')
            results = find_by_sportEvent_in_typeddict(data, sport)
            if results:
                for item in results:
                    print(format_sport_info_typedDict(item))
            else:
                print('No users with this sport event!')

    elif args.findcoach:
        if args.namedtuple:
            data = load_namedtuple_users(args.findcoach)
            coach = input('Coach to find: ')
            results = find_by_coachSurname_in_namedtyple(data, coach)
            if results:
                for item in results:
                    print(format_sport_info(item))
            else:
                print('No users with this coach surname!')

        elif args.dataclass:
            data = load_dataclass_users(args.findcoach)
            coach = input('Coach to find: ')
            results = find_by_coachSurname_in_dataclass(data, coach)
            if results:
                for item in results:
                    print(format_sport_info(item))
            else:
                print('No users with this coach surname!')

        else:
            data = load_typeddict_users(args.findcoach)
            coach = input('Coach to find: ')
            results = find_by_coachSurname_in_typeddict(data, coach)
            if results:
                for item in results:
                    print(format_sport_info_typedDict(item))
            else:
                print('No users with this coach surname!')

    elif args.print:
        if args.namedtuple or args.dataclass:
            data = load_namedtuple_users(args.print)
            if data:
                for item in data:
                    print(format_sport_info(item))
        else:
            data = load_typeddict_users(args.print)
            if data:
                for item in data:
                    print(format_sport_info_typedDict(item))

    else:
        print('Unknown command!')


if __name__ == "__main__":
    main()
