from program.frequency_formatter import frequency_analysis_formatter
from program.frequency_analyzer import FrequencyAnalyzer
from program.file_reader import FileReader


FILENAME = "./text1.txt"


def main():
    file_text = FileReader.get_text_from_file(FILENAME)
    analysis = FrequencyAnalyzer.frequency_analyze(file_text, OnlyLetters=False)

    frequency_analysis_formatter(analysis)


if __name__ == "__main__":
    main()
