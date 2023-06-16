from collections import deque
import sys

N = int(input())
house = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def bfs(graph, start): # 시간초과.
    q = deque([start])
    answer = 0

    # (d_row, d_col, next_status) 0 : 가로, 1: 세로, 2: 대각선
    next_status = [[(0, 1, 0), (1, 1, 2)], [(1, 0, 1), (1, 1, 2)], [(1, 1, 2), (1, 0, 1), (0, 1, 0)]]

    while q:
        row, col, status = q.popleft()
        if row == N-1 and col == N-1:
            answer += 1
            continue

        if (row == N-1 and status == 1) or (col == N-1 and status == 0):
            continue

        for dr, dc, s in next_status[status]:
            next_row = row + dr
            next_col = col + dc
            if next_row < N and next_col < N and house[next_row][next_col] == 0:
                if s == 2:
                    if house[next_row-1][next_col] == 0 and house[next_row][next_col-1] == 0:
                        q.append((next_row, next_col, s))
                else:
                    q.append((next_row, next_col, s))
    return answer

answer = 0
def dfs(row, col, status):
    global answer
    # 0 : 가로, 1: 세로, 2: 대각선
    if row == N-1 and col == N-1:
        answer += 1
        return

    if status == 0 or status == 2:
        if col + 1 < N and house[row][col+1] == 0:
            dfs(row, col + 1, 0)

    if status == 1 or status == 2:
        if row + 1 < N and house[row+1][col] == 0:
            dfs(row + 1, col, 1)

    if row + 1 < N and col + 1 < N and house[row+1][col] == 0 and house[row][col+1] == 0 and house[row+1][col+1] == 0:
        dfs(row + 1, col + 1, 2)


# print(bfs(house, (0, 1, 0))) # bfs는 시간초과났음.
dfs(0, 1, 0)
print(answer)