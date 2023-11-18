from package.types import CipherMode


class ECB(CipherMode):
    def encrypt(self, text: str, key: int) -> str:
        blocks = self.division_into_blocks(text)
        encrypted_blocks = []

        for block in blocks:
            encrypted_blocks.append(self._algorithm.encrypt(block, key))

        return "".join(encrypted_blocks)

    def decrypt(self, text: str, key: int) -> str:
        blocks = self.division_into_blocks(text)
        decrypted_blocks = []

        for block in blocks:
            decrypted_blocks.append(self._algorithm.decrypt(block, key))

        return "".join(decrypted_blocks)
