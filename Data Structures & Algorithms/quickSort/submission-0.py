# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        if (len(pairs) <= 1):
            return pairs
        pivot = pairs.pop()
        pivot_left, pivot_right = [], []
        for pair in pairs:
            key = pair.key
            if (key < pivot.key):
                pivot_left.append(pair)
            else:
                pivot_right.append(pair)
        return self.quickSort(pivot_left[::]) + [pivot] + self.quickSort(pivot_right[::])
        