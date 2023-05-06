from dataclasses import dataclass

from .frequency_analyzer import LetterCount


@dataclass
class ShannonFanoCode:
    letter: str
    probability: int
    code: str


def generate_code(letter_counters: list[LetterCount],
                *,
                ReturnCodeTable=False
                ) -> list[ShannonFanoCode] | dict[str, str]:

    fano_codes = convert_to_fano_code(letter_counters)
    generate_helper(fano_codes)

    if ReturnCodeTable:
        return get_code_table(fano_codes)

    return fano_codes


def convert_to_fano_code(
                        letter_counters: list[LetterCount]
                        ) -> list[ShannonFanoCode]:
    return list(map(
                    lambda element: ShannonFanoCode(element[0], element[1], ""), 
                    letter_counters
                    ))


def generate_helper(array: list[ShannonFanoCode]) -> None:
    if len(array) == 1:
        return
    
    split_index = partition(array)

    modificate_code(array[:split_index+1], left)
    generate_helper(array[:split_index+1])

    modificate_code(array[split_index+1:], right)
    generate_helper(array[split_index+1:])


def modificate_code(array: list[ShannonFanoCode], func) -> None:
    for element in array:
        element.code = func(element)


def partition(array: list[ShannonFanoCode]) -> int:
    sum_of_probabilities = sum(map(lambda element: element.probability, array))
    current_probability = sum_of_probabilities // 2

    current_index = 0
    current_sum = 0

    for element in array:
        current_sum += element.probability

        if current_sum >= current_probability:
            return current_index
        
        current_index += 1


def left(element: ShannonFanoCode) -> str:
    code = element.code
    return code + "0"


def right(element: ShannonFanoCode) -> str:
    code = element.code
    return code + "1"


def get_code_table(array: list[ShannonFanoCode]) -> dict[str, str]:
    return {element.letter: element.code for element in array}