from typing import List
from functools import lru_cache

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        @lru_cache(None)
        def dfs(index: int, visited_tuple: tuple) -> bool:
            if index < 0 or index >= len(arr) or index in visited_tuple:
                return False
            if arr[index] == 0:
                return True
            
            visited_set = set(visited_tuple)
            visited_set.add(index)
            visited_tuple = tuple(visited_set)
            
            return dfs(index + arr[index], visited_tuple) or dfs(index - arr[index], visited_tuple)
        
        return dfs(start, tuple())
