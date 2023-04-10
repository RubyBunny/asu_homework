from typing import Any


class ListWrapper:
    array: list
    
    def __init__(self, array: list[Any]=[]) -> None:
        self.array = array


    def __repr__(self) -> str:
        return f"{self.array}"

    def __str__(self) -> str:
        return f"{self.array}"


    def __len__(self) -> int:
        return len(self.array)


    def __getitem__(self, key):
        return self.array[key]

    def __setitem__(self):
        raise Exception("")

    def __delitem__(self, key):
        del self.array[key]


    def __iter__(self):
        return iter(self.array)



if __name__ == "__main__":
    wrapper = ListWrapper()
