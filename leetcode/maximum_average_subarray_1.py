def findMaxAverage(nums, k):
    ans = 0
    currSum = 0

    for i in range(k):
        currSum += nums[i]
    ans = currSum / k

    for i in range(k, len(nums)):
        currSum += nums[i] - nums[i-k]
        ans = max(ans, currSum / k)
    return ans


result = findMaxAverage([1,12,-5,-6,50,3],4)
print(result)
