from abc import ABC, abstractmethod
from math import ceil

from package.types.cipher_core import CipherCore


class CipherMode(ABC):
    _algorithm: CipherCore

    def __init__(self, cipher_algorithm: CipherCore) -> None:
        self._algorithm = cipher_algorithm

    @abstractmethod
    def encrypt(self, text: str, key: int) -> str:
        ...

    @abstractmethod
    def decrypt(self, text: str, key: int) -> str:
        ...

    def division_into_blocks(self, text: str) -> list[str]:
        expanded_binary_string = self.expand_binary_string(text)

        return [
            expanded_binary_string[i*64:(i+1)*64]
            for i in range(len(expanded_binary_string) // 64)
        ]

    def expand_binary_string(self, binary_string: str) -> str:
        additional_symbols_count = (
            ceil(len(binary_string) / 64) * 64) - len(binary_string)

        return "".join([binary_string, "0" * additional_symbols_count])

    def xor_blocks(self, first: str, second: str | int) -> str:
        if isinstance(second, str):
            return self.int_to_block(
                self.block_to_int(first) ^ self.block_to_int(second)
            )
        elif isinstance(second, int):
            return self.int_to_block(
                self.block_to_int(first) ^ second
            )

    def block_to_int(self, subblock: str) -> int:
        return int(subblock, 2)

    def int_to_block(self, integer: int) -> str:
        return "{:064b}".format(integer)
