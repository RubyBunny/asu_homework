from abc import ABC, abstractmethod


class CipherCore(ABC):
    @abstractmethod
    def encrypt(self, block: str, key: int) -> str:
        ...

    @abstractmethod
    def decrypt(self, block: str, key: int) -> str:
        ...
