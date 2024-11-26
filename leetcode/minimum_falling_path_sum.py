from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [ [0]*n for _ in range(m)]

        for col in range(n):
            dp[m-1][col] = matrix[m-1][col]

        for row in range(m-2,-1,-1):
            for col in range(n):
                ans = dp[row+1][col]
                if col:
                    ans = min(ans, dp[row+1][col-1])
                if col<n-1:
                    ans = min(ans, dp[row+1][col+1])
                dp[row][col] = ans + matrix[row][col]

        min_sum = 110*110
        for col in range(n):
            min_sum = min(min_sum, dp[0][col])
        return min_sum
