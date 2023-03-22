from program.frequency_analyzer import FrequencyAnalyzer
from program.cryptographer import Cryptographer
from program.file_reader import FileReader


def main():
    text_1 = FileReader.get_text_from_file("./text1.txt")
    publicAnalysis = FrequencyAnalyzer.frequency_analyze(text_1)

    KEY = list("яюэьыъщшчцхфутсрпонмлкйизжёедгвба")

    text_2 = FileReader.get_text_from_file("./text2.txt")
    cipher_text = Cryptographer.encode_text(text_2, KEY)

    cipherAnalysis = FrequencyAnalyzer.frequency_analyze(cipher_text)
    print(Cryptographer.decode_text(cipher_text[100:400], cipherAnalysis, publicAnalysis))


if __name__ == "__main__":
    main()