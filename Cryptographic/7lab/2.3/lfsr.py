class LFSR:
    register_values: list[int]
    register_indexes: list[int]

    def __init__(self, initial_values: list[int], register_indexes: list[int]) -> None:
        self.register_values = initial_values
        self.register_indexes = register_indexes = sorted(
            map(lambda value: len(self.register_values) - value, register_indexes),
        )

    def generate_key(self, length: int) -> list[int]:
        key: list[int] = []

        for _ in range(length):
            key.append(self.register_values[0])

            for index in self.register_indexes:
                self.register_values[0] ^= self.register_values[index]

            self.register_values.append(self.register_values.pop(0))

        return key
