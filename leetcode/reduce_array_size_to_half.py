from typing import List
from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        original_size = len(arr)
        target = original_size / 2
        counts = Counter(arr)
        frequency_tuples = [(freq,num) for num,freq in counts.items()]

        frequency_tuples.sort(key=lambda x: x[0], reverse=True)

        ans = 0
        curr = 0


        for freq, _ in frequency_tuples:
            curr += freq
            ans += 1
            if curr >= target:
                break
        
        return ans 
