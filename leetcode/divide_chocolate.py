from typing import List
import math

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k:int) -> int:

        if k==0:
            return sum(sweetness)

        def check(target):
            pieces = 0
            acum = 0
            for sweet in sweetness:
                acum += sweet
                if acum >= target:
                    pieces += 1
                    acum = 0
            return pieces >= k + 1

        left = min(sweetness)
        right = math.ceil(sum(sweetness)/k)

        while left <= right:
            mid = (left+right)//2
            if check(mid):
                left = mid +1
            else:
                right = mid-1


        return right 

