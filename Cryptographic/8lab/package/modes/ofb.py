from package.types import CipherMode


class OFB(CipherMode):
    def encrypt(self, text: str, key: int, initial_vector: int) -> str:
        blocks = self.division_into_blocks(text)
        key_stream = self._algorithm.encrypt(self.int_to_block(initial_vector), key)
        encrypted_blocks = [self.xor_blocks(key_stream, blocks[0])]

        for i in range(1, len(blocks)):
            key_stream = self._algorithm.encrypt(key_stream, key)
            encrypted_blocks.append(self.xor_blocks(key_stream, blocks[i]))

        return "".join(encrypted_blocks)

    def decrypt(self, text: str, key: int, initial_vector) -> str:
        blocks = self.division_into_blocks(text)
        key_stream = self._algorithm.encrypt(self.int_to_block(initial_vector), key)
        decrypted_blocks = [self.xor_blocks(key_stream, blocks[0])]

        for i in range(1, len(blocks)):
            key_stream = self._algorithm.encrypt(key_stream, key)
            decrypted_blocks.append(self.xor_blocks(key_stream, blocks[i]))

        return "".join(decrypted_blocks)
