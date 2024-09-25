from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix = []
        acum = 0
        ans = []

        for i in range(n):
            acum += nums[i]
            prefix.append(acum)

        for i in range(n):
            left  = i-k
            right = i+k

            radius = -1

            if left>=0 and right<n :
                left_sum = 0
                if(left>0):
                    left_sum = prefix[left-1]
                
                radius = (prefix[right]-left_sum) // (right - left + 1)
            


            ans.append(radius)

        return ans 

sol = Solution()
res = sol.getAverages([8],100)
print(res)
