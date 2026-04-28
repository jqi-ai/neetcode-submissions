class Node:
    def __init__(self, key, value, next=None) -> None:
        self.key = key
        self.value = value
        self.next = next

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def insert(self, key: int, value: int) -> None:
        hash = self._hash(key)
        head = self.table[hash]
        while head is not None:
            if head.key == key:
                head.value = value
                return None
            head = head.next
        
        new_node = Node(key, value, self.table[hash])
        self.table[hash] = new_node
        self.size += 1
        if self.size / self.capacity >= 0.5:
            self.resize()
        return None


    def get(self, key: int) -> int:
        hash = self._hash(key)
        head = self.table[hash]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return -1

    def remove(self, key: int) -> bool:
        hash = self._hash(key)
        head = self.table[hash]
        if head and head.key == key:
            self.table[hash] = head.next
            self.size -= 1
            return True
        while head and head.next:
            if head.next.key == key:
                head.next = head.next.next
                self.size -= 1
                return True
            head = head.next
        return False


    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        old_table = self.table
        self.capacity *= 2
        self.size = 0
        self.table = [None] * self.capacity
        for head in old_table:
            while head:
                self.insert(head.key, head.value)
                head = head.next
    
    def _hash(self, key: int) -> int:
        return key % self.capacity