from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }

        def backtrack(idx, current):
            if idx == n:
                ans.append("".join(current))
                return;

            digit = digits[idx]
            next_digits = digitMap.get(digit,[])
            for v in next_digits:
                current.append(v)
                backtrack(idx+1, current)
                current.pop()



        ans = []
        n = len(digits)

        if n==0:
            return []

        backtrack(0, [])


        return ans
