class Solution:
    def maximum69Number(self, num: int) -> int:
        number_str = str(num)
        parts = list(number_str)

        for idx in range(len(parts)):
            if parts[idx]=='6':
                parts[idx]='9'
                break

        ans = int("".join(parts))
    
        return ans
