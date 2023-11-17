from package.types import CipherMode


class CBC(CipherMode):
    def encrypt(self, text: str, key: int, initial_vector: int) -> str:
        blocks = self.division_into_blocks(text)
        encrypted_subblocks = [
            self._algorithm.encrypt(
                self.xor_blocks(blocks[0], initial_vector),
                key
            )
        ]
        for i in range(1, len(blocks)):
            encrypted_subblocks.append(
                self._algorithm.encrypt(
                    self.xor_blocks(blocks[i], encrypted_subblocks[-1]),
                    key
                )
            )

        return "".join(encrypted_subblocks)

    def decrypt(self, text: str, key: int, initial_vector: int) -> str:
        blocks = self.division_into_blocks(text)
        decrypted_blocks = [
            self.xor_blocks(
                self._algorithm.decrypt(
                    blocks[0],
                    key
                ),
                initial_vector
            )
        ]

        for i in range(1, len(blocks)):
            decrypted_blocks.append(
                self.xor_blocks(
                    self._algorithm.decrypt(
                        blocks[i],
                        key
                    ),
                    blocks[i-1]
                )
            )

        return "".join(decrypted_blocks)
