from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        def isExit(row,col,m,n):
            if row==0 or col==n-1 or row==m-1 or col==0:
                return True

            return False
        
        def isValid(row,col,m,n):
            if 0<=row<m and 0<=col<n and maze[row][col]=='.' :
                return True
            return False

        m = len(maze)
        n = len(maze[0])

        queue = deque([(entrance[0],entrance[1],0)])
        maze[entrance[0]][entrance[1]]='x'

        directions = [(-1,0),(0,1),(1,0),(0,-1)];
        

        while queue:
            row, col, dist = queue.popleft()
            if dist>0 and isExit(row,col,m,n):
                return dist

            
            for dx, dy in directions:
                next_row = row + dy
                next_col = col + dx

                if isValid(next_row, next_col, m, n):
                    maze[next_row][next_col]='x'
                    queue.append((next_row,next_col,dist+1))

        return -1
