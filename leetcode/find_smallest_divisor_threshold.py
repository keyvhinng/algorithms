from typing import List
import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(divisor):
            sum = 0
            for num in nums:
                sum += math.ceil(num/divisor)
            return sum <= threshold

        left = 1
        right = max(nums)

        while left<=right:
            mid = (left+right)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1

        return left
