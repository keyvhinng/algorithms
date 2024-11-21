from collections import deque

class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        def valid(row,col):
            return 0<=row<m and 0<=col<n

        m = len(grid)
        n = len(grid[0])
        queue = deque([0,0,k,0])
        seen = {(0,0,k)}
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        while queue:
            row, col, remain, steps = queue.popleft()
            if row==m-1 and col==n-1:
                return steps
            
            for dx, dy in directions:
                next_row, next_col = row+dy, col+dx
                if valid(next_row, next_col):
                    if grid[next_row][next_col]==0:
                        if(next_row,next_col,remain) not in seen:
                            seen.add((next_row,next_col, remain))
                            queue.append((next_row,next_col,remain,steps+1))
                    elif remain and (next_row,next_col,remain-1) not in seen:
                        seen.add((next_row, next_col, remain-1))
                        queue.append((next_row, next_col, remain-1, steps+1))
        return -1
