from bitarray import bitarray
from math import floor
import os

from libs.frequency_formatter import frequency_analysis_formatter
from libs.frequency_analyzer import FrequencyAnalyzer
from libs.shannon_fano_code import generate_code
from libs.file_reader import FileReader


FILENAME = "./text1.txt"
ZIPNAME = "./zip_text.txt"


def main():
    file_text = FileReader.get_text_from_file(FILENAME)
    analysis = FrequencyAnalyzer.frequency_analyze(file_text, OnlyLetters=False)

    codes = generate_code(analysis, ReturnCodeTable=True)
    zip_text = "".join(map(lambda letter: codes[letter], file_text))

    for key in codes.keys():
        print(f"{key}: {codes[key]}")
    
    FileReader.write_bytes_in_file(ZIPNAME, bitarray(zip_text))

    original_size = os.path.getsize(FILENAME)
    zip_size = os.path.getsize(ZIPNAME)

    print(f"{100 - floor((zip_size / original_size * 100))}% — процент сжатия")


if __name__ == "__main__":
    main()