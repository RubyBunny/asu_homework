from package.md5 import md5
from package.rsa import RSA
from package.file_reader import FileReader
from package.util import convert_bytes2string


def main() -> None:
    rsa = RSA(19, 41, 691)  # 41 59, 23 71
    msg = FileReader.get_text_from_file("./input.txt")
    hash_msg = md5(msg.encode())

    print(f"Открытый ключ: {rsa.e, rsa.n}")
    print(f"Закрытый ключ: {rsa.d, rsa.n}")
    print(f"Хеш открытого текста: {hash_msg}")

    signature = rsa.encrypt(hash_msg)
    FileReader.write_text_in_file("./signature.txt", convert_bytes2string(signature))

    hash_signature = convert_bytes2string(rsa.decrypt(convert_bytes2string(signature)))

    print(f"Хеш подписи: {hash_signature}")
    print(
        "Подпись", "действительна" if hash_signature == hash_msg else "не действительна"
    )


if __name__ == "__main__":
    main()
