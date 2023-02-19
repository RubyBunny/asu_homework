from frequency_analyzer import FrequencyAnalyzer
from frequency_analysis_formatter import frequency_analysis_formatter
from argparse import ArgumentParser


def main():
    analyzer = FrequencyAnalyzer("text.txt")
    frequency_analysis_formatter(analyzer.frequency_analyse())

if __name__ == "__main__":
    main()
