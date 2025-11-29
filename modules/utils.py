from collections import deque

class LogQueue:
    def __init__(self):
        # Modul 1: Variabel & Tipe Data (Deque sebagai Queue)
        self.__queue = deque()

    # Modul 4: Method/Function
    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.__queue.popleft()
        return None

    def is_empty(self):
        # Modul 3: Pengkondisian (Return boolean)
        return len(self.__queue) == 0