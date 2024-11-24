import heapq
import math
from typing import List

class Solution:
    def minStoneSum(self, piles: List[int], k:int) -> int:
        piles = [-x for x in piles]
        heapq.heapify(piles)
        ans = 0

        for i in range(k):
            num = heapq.heappop(piles)
            print(num)
            nnum = math.floor(num/2)
            print(nnum)
            heapq.heappush(piles, nnum) 

        for i in range(len(piles)):
            ans += piles[i]

        return ans
