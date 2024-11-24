from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int])-> List[int]:
        curr = 0
        acum = []

        nums.sort()

        def binary_search(arr, target):
            left = 0
            right = len(arr)-1
            found = False
            idx = 0

            while left<=right:
                mid = (left+right)//2

                if arr[mid] == target:
                    found = True
                    idx = mid
                    break
                if arr[mid]>target:
                    right = mid-1
                else:
                    left = mid+1

            if not found:
                idx = left - 1

            return idx

        for num in nums:
            curr += num
            acum.append(curr)

        return [binary_search(nums, query) + 1 for query in queries]

