class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set()
        stones_count = defaultdict(int)
        ans = 0

        for c in jewels:
            jewels_set.add(c)
        
        for c in stones:
            if c in jewels_set:
                ans += 1

        return ans





