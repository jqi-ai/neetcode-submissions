class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(weight)
        dp = [[0] * (capacity + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            currentWeight = weight[i - 1]
            currentValue = profit[i - 1]
            for w in range(1, capacity + 1):
                if (currentWeight <= w):
                    dp[i][w] = max(currentValue + dp[i - 1][w - currentWeight], dp[i - 1][w])
                else:
                    dp[i][w] = dp[i - 1][w]
        return dp[n][capacity]
        