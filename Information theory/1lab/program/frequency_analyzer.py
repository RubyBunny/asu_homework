from collections import Counter
import re


class FrequencyAnalyzer:

    @classmethod
    def frequency_analyze(cls, text: str) -> list[str]:
        letter_counter = cls.__get_letter_count(text)
        letter_counter.sort(reverse=True, key=lambda letter_tuple: letter_tuple[1])

        return list(map(lambda tup: tup[0], letter_counter)), letter_counter


    @classmethod
    def __get_letter_count(cls, text: str) -> list[tuple]:
        counter = Counter(re.compile('[^а-яА-яёЁ]').sub("", text))
        return list(counter.items())

