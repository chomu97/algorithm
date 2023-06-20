"""시간 초과 풀이
N = int(input())
answer = 0
def put_queen(row, col, board):
    new_board = [b[:] for b in board]
    for i in range(N):
        for j in range(N):
            if i == row or j == col:
                new_board[i][j] = 1

    d = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for i in range(-N, N):
        for dy, dx in d:
            drow = row + dy * i
            dcol = col + dx * i
            if 0 <= drow < N and 0 <= dcol < N:
                new_board[drow][dcol] = 1
    return new_board

def dfs(row, col, visited, queens):
    global answer
    if N * N - sum(sum(v) for v in visited) >= N - queens:
        if queens == N:
            answer += 1
            return
        new_visited = put_queen(row, col, visited)
        if row < N-1:
            for c in range(N):
                if new_visited[row + 1][c] == 0:
                    dfs(row + 1, c, new_visited, queens+1)

import time
start = time.time()
for i in range(N):
    visited = [[0] * N for _ in range(N)]
    dfs(0, i, visited, 1)
end = time.time()
print(answer)
print(f"{end - start:.5f} sec")
"""


"""이것도 시간초과.
# 같은 열 체크 : col[i] => i번째 행에 있는 queen이 놓여 있는 column의 위치. 만약 col[i] == col[k] 이면 불가능.
# 대각선 체크 : abs(col[i] - col[k]) == abs(i - k) 이면 대각선.
# 왼쪽에서 위협하는 퀸은 col[i] - col[k] == i - k, 오른쪽에서 위협하는 퀸은 col[i] - col[k] == k - i ( i, k 는 행 번호이므로 )

N = int(input())
answer = 0
col = [0] * (N+1)
def n_queens(i, col):
    global answer
    n = len(col) - 1
    if promising(i, col):
        if i == n:
            answer += 1
            # print(col[1:n+1])
        else:
            for j in range(1, n+1):
                col[i+1] = j
                n_queens(i+1, col)


def promising(i, col):
    k = 1
    flag = True
    while k < i and flag:
        if col[i] == col[k] or abs(col[i] - col[k]) == abs(i-k):
            flag = False
        k += 1
    return flag

n_queens(0, col)
print(answer)
"""

N = int(input())
answer = 0
col = [0] * N
diag = [0] * (2 * N) # 오른쪽 위로 향하는 대각선의 경우 col+row 값이 동일하므로 row+col 로 확인 가능하다.
diag2 =[0] * (2 * N) # 왼쪽 위로 향하는 대각선의 경우 row-col 값이 동일하므로 row-col로 확인 가능하다. ( -여도 문제없음, -1 인덱싱이 가능하므로)

def dfs(i): # i 행에 퀸을 놓는 경우.
    global answer
    if i == N:
        answer += 1
        return
    else:
        for j in range(N):
            if col[j] == diag[i+j] == diag2[j - i] == 0:
                col[j] = diag[i+j] = diag2[j-i] = 1 # 열, 대각선 체크
                dfs(i+1)
                col[j] = diag[i+j] = diag2[j-i] = 0 # 체크 해제

dfs(0)
print(answer)

