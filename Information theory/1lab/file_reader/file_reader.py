class FileReader:
    
    __filename: str

    def __init__(self, filename: str) -> None:
        self.__filename = filename

    def get_text_from_file(self) -> str:
        with open(self.__filename, "r", encoding="utf-8") as file:
            text = file.read()

        return text.lower()

    def create_file_copy(self, copy_name: str="copy.txt"):
        with open(copy_name, 'w', encoding="utf-8") as copy:
            copy.write(self.get_text_from_file())