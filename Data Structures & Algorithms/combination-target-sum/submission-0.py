class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(curr, index, left):
            nonlocal res
            if index >= len(nums):
                return
            if left < 0:
                return
            if left == 0:
                if curr not in res:
                    res.append(curr[:])
                return
            backtrack(curr + [nums[index]], index, left - nums[index])
            backtrack(curr, index + 1, left)
            

        backtrack([], 0, target)
        return [list(item) for item in res]