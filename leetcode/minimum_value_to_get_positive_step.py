from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        acum = 0
        n = len(nums)
        currMin = 100*101 

        for i in range(n):
            acum += nums[i]
            if acum < currMin:
                currMin = acum
        
        ans = 1
        if currMin < 0 :
            ans = abs(currMin) + 1

        return ans


sol = Solution()
res = sol.minStartValue([-3,2,-3,4,2])
print(res)
