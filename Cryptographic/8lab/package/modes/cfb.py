from package.types import CipherMode


class CFB(CipherMode):
    def encrypt(self, text: str, key: int, initial_vector: int) -> str:
        blocks = self.division_into_blocks(text)
        encrypted_blocks = [
            self.xor_blocks(
                self._algorithm.encrypt(self.int_to_block(initial_vector), key),
                blocks[0],
            )
        ]

        for i in range(1, len(blocks)):
            encrypted_blocks.append(
                self.xor_blocks(
                    self._algorithm.encrypt(encrypted_blocks[-1], key),
                    blocks[i],
                )
            )

        return "".join(encrypted_blocks)

    def decrypt(self, text: str, key: int, initial_vector: int) -> str:
        blocks = self.division_into_blocks(text)
        decrypted_blocks = [
            self.xor_blocks(
                self._algorithm.encrypt(self.int_to_block(initial_vector), key),
                blocks[0],
            )
        ]

        for i in range(1, len(blocks)):
            decrypted_blocks.append(
                self.xor_blocks(
                    self._algorithm.encrypt(blocks[i - 1], key),
                    blocks[i],
                )
            )

        return "".join(decrypted_blocks)
