from typing import List, Tuple
from collections import Counter
import re


class FrequencyAnalyzer:

    @classmethod
    def frequency_analyze(cls, text: str) -> List[Tuple]:
        letter_counter = cls.__get_letter_count(text)
        letter_counter.sort(reverse=True, key=lambda letter_tuple: letter_tuple[1])

        return letter_counter


    @classmethod
    def __get_letter_count(cls, text: str) -> List[Tuple]:
        counter = Counter(re.compile('[^а-яА-я]').sub("", text))
        return list(counter.items())

