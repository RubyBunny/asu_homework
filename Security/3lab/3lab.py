import os
import sys
import time
import json
from random import randint


def read_json() -> list[list[int]]:
    with open("./array.json", "r") as file:
        array = json.load(file)

    return array


def write_json(data: list[list[int]]) -> None:
    with open("./array.json", "w") as file:
        file.write(json.dumps(data))


def generate_matrix(n: int, m: int) -> list[list[int]]:
    return [[
        randint(-10, 10) for _ in range(m)
    ] for _ in range(n)]


def local_max_count(row: list[int]) -> int:
    count = 0

    for i in range(1, len(row) - 1):
        if row[i-1] < row[i] and row[i] > row[i+1]:
            count += 1

    return count


def main() -> None:

    print(
        f"Parent\tPID: {os.getpid()}  UID: {os.getppid()}  GID: {os.getgid()}")

    write_json(generate_matrix(5, 55))
    array = read_json()

    for i in range(5):

        parent_pid = os.fork()

        if not parent_pid:
            print(
                f"Child\tPID: {os.getpid()}  UID: {os.getppid()}  GID: {os.getgid()}")

            time.sleep(1)

            row = array[i]
            print(local_max_count(row), f"- Child {i+1}")
            sys.exit(i)

    os.system("pstree")

    for i in range(5):
        os.wait()


if __name__ == "__main__":
    main()
