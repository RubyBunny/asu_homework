#==========================================
# ПРОЧИТАТЬ И УДАЛИТЬ ПЕРЕД ИСПОЛЬЗОВАНИЕМ   
#==========================================
# В задаче (4—5 лабораторная) требовалось вынести код (алгоритм) сортировки в отдельный модуль (файл)
# и импортировать его в Jupyter Notebook
#
# По поводу реализации:
#
# Я реализовал отдельный модуль через класс для собственного удобства
# это не обязательно и можно ограничиться только функциями
# В СЛУЧАЕ КЛАССА МОГУТ СПРОСИТЬ ПОЧЕМУ ТАК СДЕЛАЛИ!!!
#
#
# Как импортировать модуль (файл):
#
# Модуль должен лежать в той же самой директории где Jupyter Notebook или ниже
# from папка.файл import функция/класс
# from Sort import oddEvenSort
#
# В случае если модуль (файл) лежит в более высокой директории
# from ...Sort import oddEvenSort    .. — означают "на одну директорию вверх"


def oddEvenSort(array: list) -> list:
    arr_len = len(array)

    for i in range(arr_len):
        start_point = 0 if i % 2 == 0 else 1
        for j in range(start_point, arr_len - 1, 2):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    
    return array


class Sort:

    @classmethod
    def __heapify(cls, arr, n, i):
        root = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            root = l

        if r < n and arr[root] < arr[r]:
            root = r

        if root != i:
            arr[i],arr[root] = arr[root],arr[i]

            cls.__heapify(arr, n, root)

    @classmethod
    def heapSort(cls, arr):
        n = len(arr)

        for i in range(n, -1, -1):
            cls.__heapify(arr, n, i)

        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            cls.__heapify(arr, i, 0)
        
        return arr