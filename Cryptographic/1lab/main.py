from libs.cipher import Cipher, Mode
from libs.file_reader import FileReader

SHIFT = 3
KEY = "паролб"


def main():
    original_text = FileReader.get_text_from_file("./input.txt")

    caesar_text = Cipher.caesar(original_text, SHIFT, mode=Mode.encode)
    vigener_text = Cipher.vigener(original_text, KEY, mode=Mode.encode)

    FileReader.write_text_in_file("caesar.txt", caesar_text)
    FileReader.write_text_in_file("vigener.txt", vigener_text)

    caesar_text = Cipher.caesar(caesar_text, SHIFT, mode=Mode.decode)
    vigener_text = Cipher.vigener(vigener_text, KEY, mode=Mode.decode)

    FileReader.write_text_in_file("caesar_orig.txt", caesar_text)
    FileReader.write_text_in_file("vigener_orig.txt", vigener_text)


if __name__ == "__main__":
    main()
