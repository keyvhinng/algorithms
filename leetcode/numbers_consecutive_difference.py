from typing import List
from functools import reduce

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []

        def backtrack(curr):
            if len(curr) == n:
                num = reduce(lambda x, y:  x*10 + y, curr)
                ans.append(num)
                return

            if len(curr) == 0:
                for i in range(1,10):
                    curr.append(i)
                    backtrack(curr)
                    curr.pop()
            else:
                last = curr[-1]
                low = last-k
                if 0 <= low <= 9:
                    curr.append(low)
                    backtrack(curr)
                    curr.pop()
                high = last+k
                if 0 <= high <= 9 and low!=high:
                    curr.append(high)
                    backtrack(curr)
                    curr.pop()
            return

        backtrack([])

        return ans
