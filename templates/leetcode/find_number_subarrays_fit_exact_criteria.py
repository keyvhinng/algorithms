from collections import defaultdict

def fn(arr, k):
    counts = defaultdict(int)
    counts[0] = 1
    ans = 0
    curr = 0

    for num in nums:
        # do some logic to change curr
        ans += counts[curr-k]
        counts[curr] += 1

    return ans
