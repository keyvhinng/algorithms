from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def valid(chars):
            st = []
            for c in chars:
                if c == '(':
                    st.append('(')
                else:
                    if len(st)>0 and st[-1]=='(':
                        st.pop()
                    else:
                        return False
            return len(st) == 0

        def backtrack(idx,current):
            if idx==2*n:
                if(valid(current)):
                    ans.append("".join(current))
                return
            
            current.append('(')
            backtrack(idx+1, current)
            current.pop()
            current.append(')')
            backtrack(idx+1, current)
            current.pop()
            return

        ans = []

        backtrack(0,[])

        return ans

