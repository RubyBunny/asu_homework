def frequency_analysis_formatter(letter_counter_list):
    for letter_tuple in letter_counter_list:
        print(f"'{letter_tuple[0]}': {letter_tuple[1]}")
