import numpy as np
from multiprocessing.shared_memory import SharedMemory


data_shm = SharedMemory(name="aaa", create=False)
array = np.ndarray((5, 30), dtype=np.int64, buffer=data_shm.buf)


def find_smallest_height(arr: list[int]) -> int:
    str_arr = "".join(map(lambda x: str(x) if x < 0 else " ", arr)).split(" ")
    length_arr = list(map(lambda x: len(x) // 2, str_arr))
    filtered_arr = list(filter(lambda x: x > 1, length_arr))

    if len(filtered_arr) != 0:
        return min(filtered_arr)

    return 0


answer_arr = np.ndarray((5,), dtype=np.int64)
for i in range(len(array)):
    answer_arr[i] = find_smallest_height(array[i])


answer_shm = SharedMemory(name="bbb", create=True, size=array.nbytes)
shared_array = np.ndarray(
    answer_arr.shape, dtype=answer_arr.dtype, buffer=answer_shm.buf
)
shared_array[:] = answer_arr[:]

data_shm.close()
answer_shm.close()

input()
