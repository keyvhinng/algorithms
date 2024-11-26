from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(idx, curr):
            if len(curr)==k:
                if sum(curr)==n:
                    ans.append(curr[:])
                return
            
            for num in range(idx,10):
                curr.append(num)
                backtrack(num+1, curr)
                curr.pop()
            return

        ans = []
        backtrack(1, [])

        return ans
