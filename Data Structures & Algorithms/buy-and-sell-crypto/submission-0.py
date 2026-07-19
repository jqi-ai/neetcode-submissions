class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (len(prices) <= 1):
            return 0
        res = 0
        current_min = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < current_min:
                current_min = prices[i]
            else:
                res = max(res, prices[i] - current_min)
        return res