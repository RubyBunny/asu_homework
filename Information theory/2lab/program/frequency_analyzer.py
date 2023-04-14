from collections import Counter

from .local_types import LetterCount


class FrequencyAnalyzer:

    @classmethod
    def frequency_analyze(cls, text: str, OnlyLetters=None) -> list[str] | list[LetterCount]:
        letter_counter = cls.__get_letter_count(text)
        letter_counter.sort(reverse=True, key=lambda letter_tuple: letter_tuple[1])

        if (OnlyLetters):
            return list(map(lambda tup: tup[0], letter_counter))
        
        return letter_counter


    @classmethod
    def __get_letter_count(cls, text: str) -> list[LetterCount]:
        counter = Counter(text)
        return list(counter.items())
