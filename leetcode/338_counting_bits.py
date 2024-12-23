from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)

        for i in range(1,n+1):
            ans[i] = ans[i-1] if i%2 else ans[i//2] 

        return ans
        
