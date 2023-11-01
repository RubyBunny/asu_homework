from lfsr import LFSR
from cipher import Cryptographer
from file_reader import FileReader


LFSR1_LENGTH = 29
LFSR2_LENGTH = 37
LFSR3_LENGTH = 27


def main():
    message = FileReader.get_text_from_file("./input.txt")
    key_length = len(message)

    lfsr1 = LFSR([1] * LFSR1_LENGTH, [3]).generate_key(key_length)
    lfsr2 = LFSR([1] * LFSR2_LENGTH, [3]).generate_key(key_length)
    lfsr3 = LFSR([1] * LFSR3_LENGTH, [3]).generate_key(key_length)

    print_key(lfsr1)
    print_key(lfsr2)
    print_key(lfsr3)

    geffe_key = [
        (lfsr1[i] & lfsr2[i]) | (~lfsr1[i] & lfsr3[i]) for i in range(key_length)
    ]

    print_key(geffe_key)

    FileReader.write_text_in_file(
        "./output.txt", Cryptographer.gamming(message, geffe_key)
    )

    print(
        f"T = {(2**LFSR1_LENGTH - 1) * (2**LFSR2_LENGTH - 1) * (2**LFSR3_LENGTH - 1)}"
    )


def print_key(key_list: list[int]) -> None:
    print("".join(map(str, key_list)), end="\n\n")


if __name__ == "__main__":
    main()
