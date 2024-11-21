import heapq 
from typing import List

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        n = len(sticks)
        if n == 0 :
            return 0

        ans = 0
        heapq.heapify(sticks)
        for _ in range(1,n):
            min1 = heapq.heappop(sticks)
            min2 = heapq.heappop(sticks)
            combine = min1 + min2
            ans += combine 
            heapq.heappush(sticks,combine)
        return ans
