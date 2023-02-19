from typing import List, Tuple
from collections import Counter
import re


class FrequencyAnalyzer:

    __filename: str

    def __init__(self, filename: str) -> None:
        self.__filename = filename


    def frequency_analyse(self) -> List[Tuple]:
        letter_counter = self.__get_letter_count()
        letter_counter.sort(reverse=True, key=lambda letter_tuple: letter_tuple[1])

        return letter_counter


    def __get_letter_count(self) -> List[Tuple]:
        text = self.__read_file_and_get_text()
        counter = Counter(re.compile('[^а-яА-я]').sub("", text))

        return list(counter.items())


    def __read_file_and_get_text(self) -> str:
        with open(self.__filename, "r", encoding="utf-8") as file:
            text = file.read()

        return text.lower()


if __name__ == "__main__":
    from frequency_analysis_formatter import frequency_analysis_formatter
    analyzer = FrequencyAnalyzer("text.txt")
    frequency_analysis_formatter(analyzer.frequency_analyse())
