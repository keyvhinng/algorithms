from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state: [day][holding][cooldown]

        n = len(prices)
        dp = [[ [0]*2 for _ in range(2) ] for __ in range(n+1)]

        for i in range(n-1,-1,-1):
            for holding in range(2):
                for cooldown in range(2):
                    ans = dp[i+1][holding][1] # skip
                    if holding:
                        ans = max(ans, dp[i+1][0][0] + prices[i]) # sell
                    elif cooldown:
                        ans = max(ans, dp[i+1][1][0] - prices[i]) # buy
                    dp[i][holding][cooldown] = ans

        return dp[0][0][0]
