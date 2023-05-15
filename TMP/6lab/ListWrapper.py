from uuid import uuid1


class ListWrapper:
    
    array: list

    def __init__(self, array: list=[]) -> None:
        self.array = list(map(lambda item: (uuid1().int, item), array.copy()))

    def __repr__(self) -> str:
        return f"{self.array}"

    def __str__(self) -> str:
        return f"{self.array}"

    def __len__(self) -> int:
        return len(self.array)

    def __getitem__(self, index: int):
        return self.array[index]

    def __iter__(self):
        return iter(self.array)

    def __delitem__(self, index: int):
        del self.array[index]

    def __setitem__(self, index, new_value):
        raise Exception("Can't set item")

    def insert(self, item):
        self.array.append(item)

    def find(self, item_id: int) -> int:
        low = 0
        high = len(self.array) - 1

        while low <= high:
            mid = (low + high) // 2
            mid_val = self.array[mid][0]

            if mid_val == item_id:
                return mid
            
            if mid_val > item_id:
                high = mid - 1
            
            else:
                low = mid + 1

        return len(self.array)
    
    def __contains__(self, item_id):
        low = 0
        high = len(self.array) - 1

        while low <= high:
            mid = (low + high) // 2
            mid_val = self.array[mid][0]

            if mid_val == item_id:
                return True
            
            if mid_val > item_id:
                high = mid - 1
            
            else:
                low = mid + 1

        return False