from multiprocessing.shared_memory import ShareableList
from multiprocessing.managers import SharedMemoryManager


class SMM:
    __shared_memory_manager = SharedMemoryManager()
    __shareable_list: ShareableList[int]

    def __init__(self) -> None:
        self.__shared_memory_manager.start()
        self.__shareable_list = self.__shared_memory_manager.ShareableList(
            [0 for _ in range(10)]
        )

    def __del__(self) -> None:
        self.__shared_memory_manager.shutdown()

    def read_list(self) -> list[int]:
        return [self.__shareable_list[i] for i in range(10)]

    def modificate_list(self, index: int, value: int) -> None:
        self.__shareable_list[index] = value
