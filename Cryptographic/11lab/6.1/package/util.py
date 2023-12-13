def extended_euclidean_algorithm(a: int, b: int) -> tuple[int, int]:
    x, x_old, y, y_old = 1, 0, 0, 1

    while b:
        q = a // b
        a, b = b, a % b
        x, x_old = x_old, x - x_old * q
        y, y_old = y_old, y - y_old * q

    return (x, y)


def euler_function(p: int, q: int) -> int:
    return (p - 1) * (q - 1)


def convert_bytes2string(byte_list: list[int]) -> str:
    return "".join(list(map(chr, byte_list)))


if __name__ == "__main__":
    print(extended_euclidean_algorithm(240, 46))
