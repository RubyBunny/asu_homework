from pyescrypt import Yescrypt, Mode

from package.smm import SMM


class User:
    __hashed_password: str
    __permissions: int
    __smm: SMM

    def __init__(self, smm: SMM, hashed_password: str, permissions: int = 1) -> None:
        self.__hashed_password = hashed_password
        self.__smm = smm
        self.chmod(permissions)

    def chmod(self, permissions: int) -> None:
        if permissions <= 0 and permissions >= 3:
            raise Exception("Wrong permissions")

        self.__permissions = permissions

    def compare_password(self, password: str) -> bool:
        try:
            Yescrypt(mode=Mode.MCF).compare(
                password.encode(), self.__hashed_password.encode()
            )
            return True
        except:
            return False

    def read_memory(self) -> list[int]:
        if self.__permissions & 1 != 0:
            return self.__smm.read_list()

        raise Exception("Access denied")

    def modificate_memory(self, index: int, value: int) -> None:
        if self.__permissions & 2 != 0:
            self.__smm.modificate_list(index, value)
            return

        raise Exception("Access denied")
