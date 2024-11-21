from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        i = 0
        j = len(people)-1
        people.sort()

        while i<=j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            ans += 1
        return ans
