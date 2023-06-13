import sys
n, m = map(int, input().split())
nums = []
for _ in range(n):
    nums.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[i][0] = dp[i-1][0] + nums[i][0]
    dp[0][i] = dp[0][i-1] + nums[0][i]
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + nums[i][j]

for i in range(n):
    dp[i] = [0] + dp[i]
dp.insert(0, [0] * (n+1))

for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    print(dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1])