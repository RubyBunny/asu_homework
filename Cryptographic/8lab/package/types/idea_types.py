class IDEANum(int):
    value: int

    def __init__(self, num: int) -> None:
        self.value = num

    @staticmethod
    def from_binary_string(binary_string: str):
        return IDEANum(int(binary_string, 2))

    def multiplicative_inversion(self):
        m = 2**16 + 1
        return IDEANum(pow(self.value, m - 2, m))

    def additive_inversion(self):
        return IDEANum(2**16 - self.value)

    def __add__(self, other):
        return IDEANum((self.value + other.value) % 2**16)

    def __mul__(self, other):
        other.value = 2**16 if other.value == 0 else other.value
        return IDEANum((self.value * other.value) % (2**16 + 1))

    def __xor__(self, other):
        return IDEANum(self.value ^ other.value)

    def __setitem__(self, other):
        self.value = other.value

    def __repr__(self) -> str:
        return f"{self.value}"
