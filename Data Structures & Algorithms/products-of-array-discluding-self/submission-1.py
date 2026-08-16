class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for index, num in enumerate(nums):
            if index == len(nums) - 1:
                break
            prefix.append(prefix[-1] * num)
        suffix = [1]
        for index, num in enumerate(reversed(nums)):
            if index == len(nums) - 1:
                break
            suffix.append(suffix[-1] * num)
        suffix = list(reversed(suffix))
        return [prefix[i] * suffix[i] for i in range(len(nums))]