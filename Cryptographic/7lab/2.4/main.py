from lfsr import LFSR
from file_reader import FileReader
from cipher import Cryptographer


LFSR1_LENGTH = 30
LFSR2_LENGTH = 38
LFSR3_LENGTH = 28


def main() -> None:
    message = FileReader.get_text_from_file("./input.txt")
    key_length = len(message)

    lfsr1 = LFSR([1] * LFSR1_LENGTH, [16, 15, 1])
    lfsr2 = LFSR([1] * LFSR2_LENGTH, [16, 15, 1])
    lfsr3 = LFSR([1] * LFSR3_LENGTH, [16, 15, 1])
    lfsr4 = LFSR([1] * 17, [12])

    key = []

    for _ in range(key_length):
        F = majority_function(lfsr4.register_values, [10, 7, 3])

        xx = majority_function(lfsr1.register_values, [15, 14, 12])
        yy = majority_function(lfsr2.register_values, [16, 13, 9])
        zz = majority_function(lfsr3.register_values, [18, 16, 13])

        output_bits = [xx, yy, zz]

        if lfsr4.register_values[10] == F:
            output_bits.append(lfsr1.round())
        else:
            output_bits.append(lfsr1.register_values[0])

        if lfsr4.register_values[3] == F:
            output_bits.append(lfsr2.round())
        else:
            output_bits.append(lfsr2.register_values[0])

        if lfsr4.register_values[7] == F:
            output_bits.append(lfsr3.round())
        else:
            output_bits.append(lfsr3.register_values[0])

        for i in range(len(output_bits)):
            output_bits[0] ^= output_bits[i]

        key.append(output_bits[0])
        lfsr4.round()

    print_key(lfsr1.register_values)
    print_key(lfsr2.register_values)
    print_key(lfsr3.register_values)
    print_key(key)

    FileReader.write_text_in_file(
        "./output.txt", Cryptographer.gamming(message, key))


def majority_function(register_values: list[int], indexes: list[int]) -> int:
    assert len(indexes) == 3

    x = register_values[indexes[0]]
    y = register_values[indexes[1]]
    z = register_values[indexes[2]]

    return (x & y) | (x & z) | (y & z)


def print_key(key_list: list[int]) -> None:
    print("".join(map(str, key_list)), end="\n\n")


if __name__ == "__main__":
    main()
