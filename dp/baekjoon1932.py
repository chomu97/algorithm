N = int(input())
dp = [int(input())]
for i in range(1, N):
    curr = list(map(int, input().split()))
    temp = []
    for j in range(len(curr)):
        if j == 0:
            temp.append(dp[j] + curr[j])
        elif j == len(curr) - 1:
            temp.append(dp[j-1] + curr[j])
        else:
            temp.append(max(dp[j-1], dp[j]) + curr[j])
    dp = temp
print(max(dp))