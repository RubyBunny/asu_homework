from math import ceil


class Cryptographer:
    @staticmethod
    def gamming(message: str, key: list[int]) -> str:
        key = (key * ceil(len(message) / len(key)))[: len(message)]

        unicodes = list(map(ord, list(message)))

        for index in range(len(unicodes)):
            unicodes[index] = unicodes[index] ^ key[index]

        return "".join(map(chr, unicodes))
