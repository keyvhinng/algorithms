from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()
        ans = 0
        left = 0
        for right, c in enumerate(s):
            if c in count:
                while s[left]!=c:
                    count.remove(s[left])
                    left += 1
                left += 1
            count.add(c)
            ans = max(ans, right-left+1)
        return ans

