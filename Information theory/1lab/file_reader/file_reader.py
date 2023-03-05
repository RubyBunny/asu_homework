class FileReader:
    
    __filename: str

    def __init__(self, filename: str) -> None:
        self.__filename = filename

    def get_text_from_file(self) -> str:
        with open(self.__filename, "r", encoding="utf-8") as file:
            text = file.read()

        return text.lower()
