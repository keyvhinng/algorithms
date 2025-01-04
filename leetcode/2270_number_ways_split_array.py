from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        cum = [0] * (n+1)

        for i in range(n):
            cum[i+1] = cum[i] + nums[i]

        ans = 0
        for i in range(1, n):
            left = cum[i]
            right = cum[n] - cum[i]
            if left >= right:
                ans += 1
        return ans
