from package.types import CipherCore
from package.types import IDEANum


class IDEA(CipherCore):
    def encrypt(self, block: str, key: int) -> str:
        subkeys = self.__generate_encrypt_subkeys(key)

        subblock = self.__division_into_subblocks(block)
        for round in range(8):
            self.__round(subblock, subkeys[round])

        self.__output_conversion(subblock, subkeys[8])
        return "".join(map(lambda x: "{:016b}".format(x), subblock))

    def decrypt(self, block: str, key: int) -> str:
        subkeys = self.__generate_decrypt_subkeys(key)

        subblock = self.__division_into_subblocks(block)
        for round in range(8):
            self.__round(subblock, subkeys[round])

        self.__output_conversion(subblock, subkeys[8])
        return "".join(map(lambda x: "{:016b}".format(x), subblock))

    def __division_into_subblocks(self, block: str) -> list[IDEANum]:
        return [
            IDEANum.from_binary_string(block[i * 16 : (i + 1) * 16]) for i in range(4)
        ]

    def __round(self, subblocks: list[IDEANum], subkeys: list[IDEANum]) -> None:
        A = subblocks[0] * subkeys[0]
        B = subblocks[1] + subkeys[1]
        C = subblocks[2] + subkeys[2]
        D = subblocks[3] * subkeys[3]
        E = A ^ C
        F = B ^ D

        subblocks[0] = A ^ ((F + E * subkeys[4]) * subkeys[5])
        subblocks[1] = C ^ ((F + E * subkeys[4]) * subkeys[5])
        subblocks[2] = B ^ (E * subkeys[4] + (F + E * subkeys[4]) * subkeys[5])
        subblocks[3] = D ^ (E * subkeys[4] + (F + E * subkeys[4]) * subkeys[5])

    def __output_conversion(
        self, subblock: list[IDEANum], subkeys: list[IDEANum]
    ) -> None:
        copy_subblock = subblock[1]
        subblock[0] *= subkeys[0]
        subblock[1] = subblock[2] + subkeys[1]
        subblock[2] = copy_subblock + subkeys[2]
        subblock[3] *= subkeys[3]

    def __generate_encrypt_subkeys(self, key: int) -> list[list[IDEANum]]:
        base_subkeys = self.__generate_base_subkeys(key)
        return self.__split_on_round_subkeys(base_subkeys)

    def __generate_decrypt_subkeys(self, key: int) -> list[list[IDEANum]]:
        base_subkeys = self.__generate_base_subkeys(key)
        inverted_subkeys = self.__change_order_list(
            self.__split_on_round_subkeys(base_subkeys)
        )
        return inverted_subkeys

    def __generate_base_subkeys(self, key: int) -> list[IDEANum]:
        bin_password = "{:0128b}".format(key)
        round_subkeys = []

        for _ in range(7):
            for i in range(8):
                round_subkeys.append(
                    IDEANum.from_binary_string(bin_password[i * 16 : (i + 1) * 16])
                )
            bin_password = bin_password[25:] + bin_password[:25]

        return round_subkeys[:-4]

    def __split_on_round_subkeys(self, subkeys: list[IDEANum]) -> list[list[IDEANum]]:
        return [subkeys[i * 6 : (i + 1) * 6] for i in range(9)]

    def __change_order_list(self, subkeys: list[list[IDEANum]]) -> list[list[IDEANum]]:
        subkeys = subkeys[::-1]
        decrypt_subkeys = [
            [*self.__inverse_subkeys(subkeys[i][:4], i), *subkeys[i + 1][4:]]
            for i in range(len(subkeys) - 1)
        ]
        decrypt_subkeys.append(self.__inverse_subkeys(subkeys[-1][:4], 0))

        return decrypt_subkeys

    def __inverse_subkeys(self, subkeys: list[IDEANum], i: int) -> list[IDEANum]:
        if i > 0 and i < 8:
            subkeys[1], subkeys[2] = subkeys[2], subkeys[1]
        subkeys[0] = subkeys[0].multiplicative_inversion()
        subkeys[1] = subkeys[1].additive_inversion()
        subkeys[2] = subkeys[2].additive_inversion()
        subkeys[3] = subkeys[3].multiplicative_inversion()

        return subkeys
