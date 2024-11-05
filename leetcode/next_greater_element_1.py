
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater_map = {}
        stack = []
        result = []

        n = len(nums2)

        for i in range(n):
            num = nums2[i]
        
            while len(stack) and num>stack[-1]:
                top = stack[-1]
                next_greater_map[top] = num 
                stack.pop()

            stack.append(num)

        for num in nums1:
            if num in next_greater_map:
                result.append(next_greater_map[num])
            else:
                result.append(-1)

        return result
        

s = Solution()
result = s.nextGreaterElement([4,1,2],[1,3,4,2])
print(result)
