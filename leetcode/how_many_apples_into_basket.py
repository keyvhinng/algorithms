from typing import List

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        curr_weight = 0
        ans = 0
        for w in weight:
            if curr_weight + w > 5000:
                break
            ans += 1
            curr_weight += w
        return ans 
