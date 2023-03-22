class FileReader:

    @staticmethod
    def get_text_from_file(filename: str) -> str:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        return text.lower()


    @staticmethod
    def write_text_in_file(filename: str, text: str):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)