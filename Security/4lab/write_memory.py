import numpy as np
from multiprocessing import shared_memory


array = np.random.randint(-10, 10, size=(5, 30))
shm = shared_memory.SharedMemory(name="aaa", create=True, size=array.nbytes)
shared_array = np.ndarray(array.shape, dtype=array.dtype, buffer=shm.buf)
shared_array[:] = array[:]

shm.close()

input()
