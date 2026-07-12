class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(weight)
        dp = [0] * (capacity + 1)
        for w in range(1, capacity + 1):
            for i in range(0, n):
                if weight[i] <= w:
                    dp[w] = max(dp[w], profit[i] + dp[w - weight[i]])
        return dp[capacity]