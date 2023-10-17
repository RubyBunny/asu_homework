from tqdm import tqdm


class LFSR:
    register_values: list[int]

    def __init__(self, initial_values: list[int]) -> None:
        self.register_values = initial_values

    def generate_key(self, register_indexes: list[int]) -> list[int]:
        key: list[int] = []
        register_indexes = sorted(
            map(lambda value: len(self.register_values) - value, register_indexes),
        )

        for _ in tqdm(range(2 ** len(self.register_values))):
            key.append(self.register_values[0])

            for index in register_indexes:
                self.register_values[0] ^= self.register_values[index]

            self.register_values.append(self.register_values.pop(0))

        return key


if __name__ == "__main__":
    lfsr = LFSR([1 for _ in range(4)])
    key = lfsr.generate_key([1])

    print("".join(map(str, key)) == "1111010110010001")  # True
    # Проверка на примере из лекции
