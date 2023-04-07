from program.frequency_formatter import frequency_analysis_formatter
from program.frequency_analyzer import FrequencyAnalyzer
from program.cryptographer import Cryptographer
from program.file_reader import FileReader


def main():
    text_1 = FileReader.get_text_from_file("./text1.txt")
    publicAnalysis, publicCounter = FrequencyAnalyzer.frequency_analyze(text_1)

    KEY = list("яюэьыъщшчцхфутсрпонмлкйизжёедгвба")

    text_2 = FileReader.get_text_from_file("./text2.txt")
    cipher_text = Cryptographer.encode_text(text_2, KEY)

    cipherAnalysis, cipherCounter = FrequencyAnalyzer.frequency_analyze(cipher_text)

    frequency_analysis_formatter(publicCounter)
    print()
    frequency_analysis_formatter(cipherCounter)

    print(cipher_text[86:155])
    print(Cryptographer.decode_text(cipher_text[86:155], cipherAnalysis, publicAnalysis))


if __name__ == "__main__":
    main()