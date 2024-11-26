from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0]==1:
            return 0

        dp = [[0]*n for _ in range(m)]
        dp[0][0]=1

        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col]==0:
                    if row>0:
                        dp[row][col] += dp[row-1][col]
                    if col>0:
                        dp[row][col] += dp[row][col-1]


        return dp[m-1][n-1]
