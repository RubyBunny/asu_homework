from argparse import ArgumentParser, BooleanOptionalAction
from libs.cipher import Cipher, Mode
from libs.file_reader import FileReader


argparse = ArgumentParser()

cipher_algoritm_group = argparse.add_mutually_exclusive_group()
cipher_algoritm_group.add_argument(
    "-c", "--cesaer", type=bool, action=BooleanOptionalAction)
cipher_algoritm_group.add_argument(
    "-v", "--vigener", type=bool, action=BooleanOptionalAction)
cipher_algoritm_group.add_argument(
    "-g", "--gamming", type=bool, action=BooleanOptionalAction)

cipher_mode_group = argparse.add_mutually_exclusive_group()
cipher_mode_group.add_argument(
    "-e", "--encode", type=bool, action=BooleanOptionalAction)
cipher_mode_group.add_argument(
    "-d", "--decode", type=bool, action=BooleanOptionalAction)

argparse.add_argument("file", type=str)
argparse.add_argument("-k", "--key", type=str, default="пароль")

args = argparse.parse_args()


def main():
    original_text = FileReader.get_text_from_file(args.file)

    if args.cesaer:
        if args.encode:
            caesar_text = Cipher.caesar(
                original_text, int(args.key), mode=Mode.encode)
            FileReader.write_text_in_file("ouput.txt", caesar_text)
        elif args.decode:
            caesar_text = Cipher.caesar(
                original_text, int(args.key), mode=Mode.decode)
            FileReader.write_text_in_file("ouput.txt", caesar_text)

    if args.vigener:
        if args.encode:
            vigener_text = Cipher.vigener(
                original_text, args.key, mode=Mode.encode)
            FileReader.write_text_in_file("ouput.txt", vigener_text)
        elif args.decode:
            vigener_text = Cipher.vigener(
                original_text, args.key, mode=Mode.decode)
            FileReader.write_text_in_file("ouput.txt", vigener_text)

    if args.gamming:
        gamming_text = Cipher.gamming(original_text, args.key)
        FileReader.write_text_in_file("ouput.txt", gamming_text)


if __name__ == "__main__":
    main()
