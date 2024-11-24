from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def check(largest_sum):
            print('checking ' + str(largest_sum))
            sum = 0
            count = 0
            for num in nums:
                if sum + num >largest_sum:
                    sum = num
                    count += 1
                else:
                    sum += num
            count += 1
            return count==k 


        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = (left+right)//2

            if check(mid):
                print(' YES')
                right = mid-1
            else:
                left = mid+1

        return left
