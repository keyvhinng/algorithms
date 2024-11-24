from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binary_search(arr, target):
            left = 0
            right = len(arr)-1

            while left<=right:
                mid = (left+right)//2

                if arr[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left

        potions.sort()
        ans = []
        m = len(potions)

        for spell in spells:
            i = binary_search(potions, success/spell)
            ans.append(m-i)

        return ans

