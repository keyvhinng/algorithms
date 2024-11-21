import heapq
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k:int, x:int) -> List[int]:
        heap = []

        for num in arr:
            distance = abs(x-num)
            heapq.heappush(heap, (-distance, -num))
            if len(heap)>k:
                heapq.heappop(heap)

        return sorted([-pair[1] for pair in heap])
