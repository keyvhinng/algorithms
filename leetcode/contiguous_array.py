class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        n = len(nums)
        count_index = {0: -1}


        for i, num in enumerate(nums):
            count += -1 if num==0 else 1

            if count in count_index:
                ans = max(ans, i-count_index[count])
            else:
                count_index[count] = i

        return ans 
