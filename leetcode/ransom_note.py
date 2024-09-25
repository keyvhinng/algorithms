class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = defaultdict(int)
        ans = True

        for c in magazine:
            count[c] += 1

        for c in ransomNote:
            count[c] -= 1
            if count[c] < 0:
                ans = False

        return ans
                
