import sys
N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
arr = [[sys.maxsize] * N for _ in range(N)]
for i in range(N):
    arr[i][i] = 0

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    arr[a-1][b-1] = min(c, arr[a-1][b-1])

for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

for i in range(N):
    for j in range(N):
        print(arr[i][j] if arr[i][j] != sys.maxsize else 0, end=" ")
    print()

