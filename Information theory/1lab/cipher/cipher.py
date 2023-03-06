class Cipher:

    __PUBLIC_KEY = list("оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъё")
    __ALPHABET = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")

    @classmethod
    def encode_text(cls, 
                    text: str,
                    list_of_substitutions: list[str]
                    ) -> str:
        key = cls.__generate_key(cls.__ALPHABET, list_of_substitutions)
        return cls.__replace_letter(list(text), key)


    @classmethod
    def decode_text(cls, 
                    text: str,
                    list_of_occurrences: list[str]=__ALPHABET,
                    list_of_substitutions: list[str]=__PUBLIC_KEY
                    ) -> str:
        key = cls.__generate_key(list_of_occurrences, list_of_substitutions)
        return cls.__replace_letter(list(text), key)


    @staticmethod
    def __generate_key(list_of_occurrences: list[str],
                       list_of_substitutions: list[str]
                       ) -> dict[str, str]:
        key = {}
        list_of_substitutions = list_of_substitutions[:len(list_of_occurrences)]

        for index in range(len(list_of_substitutions)):
            key[list_of_occurrences[index]] = list_of_substitutions[index]

        return key


    @staticmethod
    def __replace_letter(text: list[str], key: dict[str, str]):
        for index, letter in enumerate(text):
            if letter not in key:
                continue

            text[index] = key[letter]

        return "".join(text)

