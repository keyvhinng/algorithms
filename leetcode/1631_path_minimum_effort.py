from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def valid(row,col):
            return 0<=row<m and 0<=col<n

        def check(effort):
            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            seen = {(0,0)}
            stack = [(0,0)]

            while stack:
                row, col = stack.pop()
                if (row,col) == (m-1,n-1):
                    return True

                for dx, dy in directions:
                    next_row, next_col = row+dy, col+dx
                    if valid(next_row, next_col) and (next_row, next_col) not in seen:
                        if abs(heights[next_row][next_col] - heights[row][col]) <= effort:
                            seen.add((next_row,next_col))
                            stack.append((next_row, next_col))
                return False

        m = len(heights)
        n = len(heights[0])
        left = 0
        right = max(max(row) for row in heights)

        while left <= right:
            mid = (left+right)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1

        return left
