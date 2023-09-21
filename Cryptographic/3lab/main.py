from math import log2, prod
from argparse import ArgumentParser

argparse = ArgumentParser()
argparse.add_argument("nums", nargs="+", type=int)

args = argparse.parse_args()


def exponentiation(value: int, degree: int, module: int) -> int:
    t = int(log2(degree))
    a = [(value ** (2 ** i)) % module for i in range(t+1)]
    value_in_bin = list(bin(degree))[2:]
    x = [v if int(value_in_bin[i]) != 0 else 1 for i, v in enumerate(a[::-1])]

    return prod(x) % module


def main():
    value, degree, module = args.nums
    print(exponentiation(value, degree, module))


if __name__ == "__main__":
    main()
