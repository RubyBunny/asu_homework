from uuid import uuid1

class Container:
    def __init__(self, elements):

        self._len = 0

        self._data = elements.copy()
        self._ht = {}
        k = 0
        for i in self._data:
            if str(i) not in self._ht.values():
                self._ht[k] = str(i)
                k+=1
                self._len+=1
            else: self._data.remove(i)
       
        self._rht = {}
        for key, value in self._ht.items():
            if str(value) not in self._rht:
                self._rht[str(value)] = []
            self._rht[str(value)].append(key)
        

 
    def __repr__(self):
        return f"Container: {self._ht}"
    
    def __str__(self):
        return [str(self._ht[i]) for i in self._ht]
 
    def __len__(self):
        return len(self._ht)
 
    def __getitem__(self, index):
        return self._ht[index]
 
    def __iter__(self):
        return iter(self._ht)
    
    def contains(self, element):
        #if str(element) in self._data:
        #    return True
        #else: return False
        #return str(element) in self._ht.values()

        try:
            self._rht[str(element)]
        except KeyError:
            return False
        else: return True

    def insert(self, element):
        self._ht[self._len] = str(element)
        self._rht[str(element)] = self._len
        self._len +=1

    
    def find(self, element):
        #if str(element) not in self._ht.values():
        #    return len(self._ht)
        #else:
        #    return self._rht[str(element)]

        try:
            return self._rht[str(element)]
        except KeyError:
            return len(self._ht)

            

    def __delitem__(self, index):
        try:
            del self._rht[self._ht[index]]   
            del self._ht[index]    
        except KeyError:
            return 



from heapq import *

# класс для двоичной кучи
class Heap:
    def __init__(self, array: list):
        self.heap = self.__generate_heap(array.copy())

    def __len__(self): # возвращает текущий размер кучи
        return len(self.heap)

    def __generate_heap(self, array: list):
        heap = []
        array = list(map(lambda item: (uuid1().int, item), array))
        for element in array:
            heappush(heap, element)
        
        return heap

    # удалить элемент из кучи по индексу
    def __delitem__(self, i):
        # for i in range(len(self.heap)):
        #     if self.heap[i][0] == value:
            self.__swap(i, len(self.heap)-1)
            del self.heap[-1]
            self.__move_down(i)
        
    # переместить элемент на более высокий уровень кучи (вверх)
    def __move_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index][0] < self.heap[parent][0]:
            self.__swap(index, parent)
            self.__move_up(parent)

    # переместить элемент на более нижний уровень кучи (вниз)
    def __move_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index
        
        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right
        
        if smallest != index:
            self.__swap(index, smallest)
            self.__move_down(smallest)

    # поменять местами два элемента в куче
    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __getitem__(self, index: int):
        return self.heap[index]