class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = dict()
        for index, num in enumerate(nums):
            paired = target - num
            if paired in storage:
                return [storage[paired], index]
            storage[num] = index
        return [-1, -1]