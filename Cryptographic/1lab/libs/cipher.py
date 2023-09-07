from enum import Enum
from math import ceil


class Mode(Enum):
    encode = 1
    decode = -1


class Cipher:
    @staticmethod
    def caesar(message: str, shift: int, *, mode: Mode) -> str:
        unicodes = list(map(ord, list(message)))

        for index in range(len(unicodes)):
            unicodes[index] = (unicodes[index] + shift * mode.value) % 32 + 1056
            unicodes[index] += 32 if unicodes[index] < 1072 else 0

        return "".join(map(chr, unicodes))

    @staticmethod
    def vigener(message: str, key: str, *, mode: Mode) -> str:
        key = (key * ceil(len(message) / len(key)))[: len(message)]

        unicodes = list(map(ord, list(message)))
        key_unicodes = list(map(ord, list(key)))

        for index in range(len(unicodes)):
            unicodes[index] = (
                unicodes[index] + key_unicodes[index] * mode.value
            ) % 32 + 1056
            unicodes[index] += 32 if unicodes[index] < 1072 else 0

        return "".join(map(chr, unicodes))
