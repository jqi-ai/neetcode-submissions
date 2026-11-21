class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = nums[0], nums[-1]
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] > nums[j]:
                i = mid + 1
            else:
                j = mid
        pivot = i
        i, j = 0, len(nums) - 1
        if target >= nums[pivot] and target <= nums[j]:
            i = pivot
        else:
            j = pivot - 1
        return self.bst(i, j, nums, target)
    def bst(self, l, r, nums, target):
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1