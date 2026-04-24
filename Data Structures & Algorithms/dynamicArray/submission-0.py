class DynamicArray:
    
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__size = 0
        self.__array = [None] * capacity

    # Assume i is valid
    def get(self, i: int) -> int:
        return self.__array[i]

    # Assume i is valid
    def set(self, i: int, n: int) -> None:
        if (self.__array[i] == None):
            self.__size += 1
        self.__array[i] = n
        return None

    def pushback(self, n: int) -> None:
        if (self.__size == self.__capacity):
            self.resize()
        self.__array[self.__size] = n
        self.__size += 1
        return None

    # Assume array is non-empty
    def popback(self) -> int:
        print(self.__size, self.__array, self.__capacity)
        poped = self.__array[self.__size - 1]
        self.__array[self.__size - 1] = None
        self.__size -= 1
        return poped

    def resize(self) -> None:
        self.__array.extend([None] * self.__capacity)
        self.__capacity *= 2
        return None

    def getSize(self) -> int:
        return self.__size
    
    def getCapacity(self) -> int:
        return self.__capacity