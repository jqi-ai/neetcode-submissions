class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        # Find the biggest num in the middle
        left, right = nums[0], nums[-1]
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < left:
                j = mid
            else:
                i = mid
        return -1