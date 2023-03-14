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