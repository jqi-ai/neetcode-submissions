class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = 0
        nums_dedup = set(nums)
        for num in nums:
            if (num - 1) in nums_dedup:
                continue
            candidate, start = 1, num
            while start + 1 in nums_dedup:
                candidate += 1
                start += 1
            answer = max(answer, candidate)
        return answer