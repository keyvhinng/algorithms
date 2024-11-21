import heapq
from typing import List

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target = sum(nums) / 2
        heap = [float(-num) for num in nums]
        heapq.heapify(heap)

        ans = 0
        while target>0:
            ans += 1
            x = heapq.heappop(heap)
            target += x / 2
            heapq.heappush(heap, x/2)
        return ans
