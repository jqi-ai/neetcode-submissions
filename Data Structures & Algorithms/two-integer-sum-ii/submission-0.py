class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        while start < end:
            sum_current = numbers[start] + numbers[end]
            if sum_current > target:
                end -= 1
            elif sum_current < target:
                start += 1
            else:
                return [numbers[start], numbers[end]]
        return [-1, -1]
