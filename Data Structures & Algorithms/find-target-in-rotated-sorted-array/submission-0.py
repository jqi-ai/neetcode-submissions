class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = nums[0], nums[-1]
        if target == left:
            return 0
        if target == right:
            return len(nums) - 1
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif target > left:
                j = mid
            else:
                i = mid
        return -1