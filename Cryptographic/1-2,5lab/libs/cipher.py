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
            unicodes[index] = (unicodes[index] + shift * mode.value) % 26 + 78
            unicodes[index] += 26 if unicodes[index] < 97 else 0

        return "".join(map(chr, unicodes))

    @staticmethod
    def vigener(message: str, key: str, *, mode: Mode) -> str:
        key = (key * ceil(len(message) / len(key)))[: len(message)]

        unicodes = list(map(ord, list(message)))
        key_unicodes = list(map(ord, list(key)))

        for index in range(len(unicodes)):
            unicodes[index] = (
                unicodes[index] + key_unicodes[index] * mode.value
            ) % 26 + 85
            unicodes[index] += 12 if mode.value < 0 else 0
            unicodes[index] += 26 if unicodes[index] < 97 else 0

        return "".join(map(chr, unicodes))

    @staticmethod
    def gamming(message: str, key: str) -> str:
        key = (key * ceil(len(message) / len(key)))[: len(message)]

        unicodes = list(map(ord, list(message)))
        key_unicodes = list(map(ord, list(key)))

        for index in range(len(unicodes)):
            unicodes[index] = unicodes[index] ^ key_unicodes[index]

        return "".join(map(chr, unicodes))
