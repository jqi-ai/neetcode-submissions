class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None
    def next(self):
        return self.__next
    def setNext(self, next):
        self.__next = next
        return None
    def value(self):
        return self.__value

class LinkedList:
    def __init__(self):
        self.head = Node(-1)

    def get(self, index):
        head = self.head
        while head is not None:
            head = head.next()
            if head is None:
                return -1
            if index == 0:
                return head.value()
            index -= 1
        return -1

    def insertHead(self, val):
        new_head = Node(val)
        old_head = self.head.next()
        new_head.setNext(old_head)
        self.head.setNext(new_head)

    def insertTail(self, val):
        head = self.head
        while head is not None and head.next() is not None:
            head = head.next()
        if head is not None:
            head.setNext(Node(val))

    def remove(self, index):
        head = self.head
        while head is not None:
            node = head.next()
            if node is None:
                return False
            if index == 0:
                node_child = node.next()
                head.setNext(node_child)
                node.setNext(None)
                return True
            head = node
            index -= 1
        return False

    def getValues(self):
        values = []
        head = self.head
        while head is not None:
            next_node = head.next()
            if next_node is not None:
                values.append(next_node.value())
            else:
                break
            head = next_node
        return values
