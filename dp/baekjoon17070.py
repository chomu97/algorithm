import sys

N = int(input())
house = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1
# dp[i][j][ 0: 가로 1: 세로 2: 대각선]

for i in range(2, N):
    if house[0][i] == 0:
        dp[0][i][0] = dp[0][i-1][0] # 맨 윗줄 가로는 1가지 밖에 없음. ( 벽에 막히기 전까지 )

for i in range(1, N):
    for j in range(1, N):
        # 대각선
        if house[i-1][j] == 0 and house[i][j-1] == 0 and house[i][j] == 0:
            dp[i][j][2] = sum(dp[i-1][j-1])

        # 가로, 세로
        if house[i][j] == 0:
            dp[i][j][0] = dp[i][j-1][2] + dp[i][j-1][0]
            dp[i][j][1] = dp[i-1][j][2] + dp[i-1][j][1]

print(sum(dp[N-1][N-1]))