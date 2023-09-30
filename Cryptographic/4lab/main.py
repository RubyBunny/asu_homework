def main():
    print(extended_euclidean_algorithm(276, 84))


def extended_euclidean_algorithm(a: int, b: int) -> tuple[int, int, int]:
    x, x_old, y, y_old = 1, 0, 0, 1

    while b:
        q = a // b
        a, b = b, a % b
        x, x_old = x_old, x - x_old*q
        y, y_old = y_old, y - y_old*q

    return (a, x, y)


if __name__ == "__main__":
    main()
