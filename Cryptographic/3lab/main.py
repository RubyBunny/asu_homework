from math import log2, prod
from argparse import ArgumentParser

argparse = ArgumentParser()
argparse.add_argument("value", type=int)
argparse.add_argument("degree", type=int)
argparse.add_argument("module", type=int)

args = argparse.parse_args()


def exponentiation(value: int, degree: int, module: int) -> int:
    t, value_in_bin = int(log2(degree)), list(bin(degree))[2:]
    a = [(value ** (2**i)) % module for i in range(t, -1, -1)]
    x = [v for i, v in enumerate(a) if int(value_in_bin[i])]

    return prod(x) % module


def main():
    value, degree, module = args.value, args.degree, args.module
    print(exponentiation(value, degree, module))


if __name__ == "__main__":
    main()
