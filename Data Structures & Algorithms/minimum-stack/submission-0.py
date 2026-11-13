class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mini) < 1 or val < self.mini[-1]:
            self.mini.append(val)
        else:
            self.mini.append(self.mini[-1])
        return None

    def pop(self) -> None:
        self.stack.pop()
        self.mini.pop()
        return None

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.mini[-1]
