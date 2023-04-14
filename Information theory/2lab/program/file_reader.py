class FileReader:

    @staticmethod
    def get_text_from_file(filename: str) -> str:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()


    @staticmethod
    def write_text_in_file(filename: str, text: str) -> None:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)


    @staticmethod
    def write_bytes_in_file(filename: str, bytes: bytes) -> None:
        with open(filename, 'wb') as file:
            file.write(bytes)
