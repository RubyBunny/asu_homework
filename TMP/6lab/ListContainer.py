from uuid import uuid1


class ListContainer:
    
    array: list

    """Конструктор класса"""
    def __init__(self, array: list=[]) -> None:
        self.array = list(map(lambda item: (uuid1().int, item), array.copy()))

    """Методы представления данных строкой"""
    def __repr__(self) -> str:
        return f"{self.array}"

    def __str__(self) -> str:
        return f"{self.array}"
    
    """Метод возвращающий число хранимых элементов"""
    def __len__(self) -> int:
        return len(self.array)
    
    """Метод для доступа к элементу"""
    def __getitem__(self, index: int):
        return self.array[index]
    
    """Метод для итерирования"""
    def __iter__(self):
        return iter(self.array)
    
    """Метод для вставки"""
    def insert(self, item):
        self.array.append((uuid1().int, item))
    
    """Метод для удаления"""    
    def __delitem__(self, index: int):
        del self.array[index]
    
    """Метод для проверки наличия(Метод дихотомии)"""
    def __contains__(self, item_id):
        st = 0
        fin = len(self.array) - 1

        while st <= fin:
            mid = (st + fin) // 2
            mid_val = self.array[mid][0]

            if mid_val == item_id:
                return True
            
            if mid_val > item_id:
                fin = mid - 1
            
            else:
                st = mid + 1

        return False
    
    """Метод для поиска элемента"""
    def find(self, item_id: int) -> int:
        st = 0
        fin = len(self.array) - 1
        while st <= fin:
            mid = (st + fin) // 2
            mid_val = self.array[mid][0]

            if mid_val == item_id:
                return mid
            if mid_val > item_id:
                fin = mid - 1
            else:
                st = mid + 1
                
        return False
    
    """Метод для удаления элемента(O(log(n)))"""
    def __delitem2__(self, index: int) -> int:
        st = 0
        fin = len(self.array) - 1
        IDD = self.array[index][0]
        while st <= fin:
            mid = (st + fin) // 2
            mid_val = self.array[mid][0]

            if mid_val == IDD:
                del self.array[index]
            if mid_val > IDD:
                fin = mid - 1
            else:
                st = mid + 1
                
        return False
    


