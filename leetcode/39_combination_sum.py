from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(path, start, curr):
            if curr==target:
                ans.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                num = candidates[i]
                if curr + num <= target:
                    path.append(num)
                    backtrack(path, i, curr+num)
                    path.pop()
        ans = []
        backtrack([],0,0)
        return ans
