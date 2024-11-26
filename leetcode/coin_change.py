from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        dp = [float('inf')] * (amount+1)

        dp[0] = 0

        for current_amount in range(0,amount):
            for coin in coins:
                new_amount = current_amount + coin
                if new_amount <= amount:
                    dp[new_amount] = min(dp[new_amount],dp[current_amount]+1)

        if dp[amount]==float('inf'):
            return -1
        return dp[amount]
