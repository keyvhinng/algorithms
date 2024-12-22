n = 3
weights = [1, 2, 3]
values = [6,10,12]
capacity = 5


dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for w in range(capacity+1):
        if weights[i]<=w:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i]] + values[i])


ans = dp[n][capacity]
