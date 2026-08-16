class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (len(prices) <= 1):
            return 0
        res = 0
        current_min = 101
        for i, price in enumerate(prices):
            if price < current_min:
                current_min = price
            else:
                res = max(res, price - current_min)
        return res