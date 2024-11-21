from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []

        for point in points:
            x = point[0]
            y = point[1]
            distance = x*x + y*y
            heapq.heappush(heap,(distance,x,y))
        
        for _ in range(k):
            extracted = heapq.heappop(heap) 
            ans.append([extracted[1],extracted[2]])

        return ans

