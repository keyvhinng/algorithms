from typing import List

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def distance(x1, y1, x2, y2):
            return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

        n = len(bombs)
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and distance(bombs[i][0], bombs[i][1], bombs[j][0], bombs[j][1]) <= bombs[i][2]:
                    graph[i].append(j)

        def dfs(start: int, visited: set) -> int:
            visited.add(start)
            detonated = 1
            
            for neighbor in graph[start]:
                if neighbor not in visited:
                    detonated += dfs(neighbor, visited)
            
            return detonated

        max_detonations = 0
        for i in range(n):
            max_detonations = max(max_detonations, dfs(i, set()))
        return max_detonations
