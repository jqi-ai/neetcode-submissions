# MinHeap Class Implementation
class MinHeap:
    def __init__(self):
        self.heap = []  # Initialize heap with a dummy value at index 0

    def push(self, val: int) -> None:
        """Pushes a value onto the heap."""
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def pop(self) -> int:
        """Pops the smallest value off the heap."""
        if len(self.heap) <= 0:
            return -1
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # Move the last element to the root and bubble it down.
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return root

    def top(self) -> int:
        """Returns the smallest value without popping it."""
        return self.heap[0] if len(self.heap) > 0 else -1

    def heapify(self, nums: List[int]) -> None:
        """Transforms a list into a heap in-place."""
        self.heap = [] + nums
        for i in reversed(range(len(self.heap) // 2)):
            self._bubble_down(i)

    def _bubble_up(self, index: int) -> None:
        parent = (index - 1) // 2
        while index > 0 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = (index - 1) // 2

    def _bubble_down(self, index: int) -> None:
        child = 2 * index + 1 # left child
        while child < len(self.heap):
            if child + 1 < len(self.heap) and self.heap[child] > self.heap[child + 1]:
                child += 1

            if self.heap[child] >= self.heap[index]:
                break

            self.heap[child], self.heap[index] = self.heap[index], self.heap[child]
            index = child
            child = 2 * index + 1  # left child