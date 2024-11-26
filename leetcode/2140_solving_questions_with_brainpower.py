from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n+1)
        
        for i in range(n-1,-1,-1):
            j = i + questions[i][1] + 1
            dp[i] = max(questions[i][0] + dp[min(j,n)], dp[i+1])

        return dp[0]
