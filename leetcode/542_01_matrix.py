from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        def valid(row,col):
            return 0<=row<m and 0<=col<n and mat[row][col]==1

        m = len(mat)
        n = len(mat[0])
        queue = deque()
        seen = set()

        for row in range(m):
            for col in range(n):
                if mat[row][col]==0:
                    queue.append((row,col,1))
                    seen.add((row,col))

        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        while queue:
            row, col, steps = queue.popleft()

            for dx, dy in directions:
                next_row, next_col = row+dy, col+dx
                if (next_row, next_col) not in seen and valid(next_row, next_col):
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps+1))
                    mat[next_row][next_col] = steps

        return mat
