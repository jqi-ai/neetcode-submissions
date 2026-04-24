from collections import deque


class Deque:
    def __init__(self):
        self.hi = deque()

    def isEmpty(self) -> bool:
        return len(self.hi) == 0

    def append(self, value: int) -> None:
        self.hi.append(value)

    def appendleft(self, value: int) -> None:
        self.hi.appendleft(value)

    def pop(self) -> int:
        if len(self.hi) <= 0:
            return -1
        return self.hi.pop()

    def popleft(self) -> int:
        if len(self.hi) <= 0:
            return -1
        return self.hi.popleft()
