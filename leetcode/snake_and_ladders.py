from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        # Convert label to board position
        def get_position(label: int) -> tuple[int, int]:
            label -= 1  # Convert to 0-based
            row = n - 1 - (label // n)
            col = label % n if ((n - 1 - row) % 2 == 0) else n - 1 - (label % n)
            return (row, col)
        

        queue = deque([(1, 0)])
        seen = set()
        
        while queue:
            label, steps = queue.popleft()

            for next_label in range(label + 1, min(label + 6, n * n) + 1):
                row, col = get_position(next_label)

                destination = next_label if board[row][col] == -1 else board[row][col]
                
                if destination == n * n:
                    return steps + 1
                if destination not in seen:
                    seen.add(destination)
                    queue.append((destination, steps + 1))
        
        return -1
