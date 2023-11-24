import numpy as np
from multiprocessing.shared_memory import SharedMemory


exist_shm = SharedMemory(name="aaa", create=False)
answer_shm = SharedMemory(name="bbb", create=False)

array = np.ndarray((5, 30), dtype=np.int64, buffer=exist_shm.buf)
answer_array = np.ndarray((5,), dtype=np.int64, buffer=answer_shm.buf)

print(array)
print(answer_array)

exist_shm.close()
exist_shm.unlink()

answer_shm.close()
answer_shm.unlink()
