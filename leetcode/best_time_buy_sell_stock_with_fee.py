from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # state: [day][holding]
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+1)]

        for day in range(n-1,-1,-1):
            for hold in range(2):
                ans = dp[day+1][hold] #skip
                if hold:
                    dp[day][hold] = max(ans, dp[day+1][0]+prices[day]-fee) #sell
                else:
                    dp[day][hold] = max(ans, dp[day+1][1]-prices[day]) #buy

        return dp[0][0]
