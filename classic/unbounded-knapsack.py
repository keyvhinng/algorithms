from typing import List

class Solution:
    def maximumProfit(self, profit: List[int], weigth: List[int], capacity: int) -> int:
        n = len(profit)
        dp = [ [0]*(capacity+1) for _ in range(n+1) ]

        for i in range(n-1):
            for w in range(capacity+1):
                if w + weigth[i] <= capacity:
                    dp[i][w + weigth[i]] = max(dp[i][w + weigth[i]], dp[i][w] + profit[i]);
                dp[i+1][w] = max(dp[i+1][w], dp[i][w] + profit[i]);

        return dp[n-1][capacity];

