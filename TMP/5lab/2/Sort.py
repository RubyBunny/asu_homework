def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def quick_sort(arr: list):
    if (len(arr) < 2):
        return arr

    pivot = arr.pop(int(len(arr)/2))

    less = [i for i in arr if i < pivot]
    greater = [i for i in arr if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)