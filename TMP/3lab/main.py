from fuzzy_number import *

def main():
    obj1 = FuzzyNumber(10, 4, 14)
    obj2 = FuzzyNumber(15, 3, 25)

    FuzzyNumber.show_counter()
    print(obj1 + obj2)
    print(obj1 - obj2)
    print(obj1 * obj2)
    print(obj1 / obj2)
    print(obj1.reverse())
    print(help(FuzzyNumber))


if __name__ == "__main__":
    main()