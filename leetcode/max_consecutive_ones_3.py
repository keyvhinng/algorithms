from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        curr = 0
        left = 0
        n = len(nums)

        for right in range(n):
            if nums[right] == 0:
                curr += 1

            # while not valid
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1

            # now is valid
            ans = max(ans, right - left + 1)
        return ans


sol = Solution()
res = sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3)
print(res)
