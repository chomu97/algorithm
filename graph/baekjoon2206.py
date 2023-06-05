from collections import deque
import sys

def bfs(graph):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    y_lim = len(graph)
    x_lim = len(graph[0])
    visited = [[1 for _ in range(x_lim)] for _ in range(y_lim)]
    q = deque()
    q.append((0, 0, 1, 0))
    while q:
        y, x, step, wall = q.popleft()
        print(y, x, step, wall)
        if y == y_lim-1 and x == x_lim-1:
            return step
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < y_lim and 0 <= nx < x_lim:
                if visited[ny][nx] == 1:
                    if board[ny][nx] == 0:
                        q.append((ny, nx, step+1, wall))
                    elif board[ny][nx] == 1 and wall == 0:
                        q.append((ny, nx, step+1, 1))
        visited[y][x] = 0
    return -1

def bfs2(graph):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    y_lim = len(graph)
    x_lim = len(graph[0])
    visited = [[[False, False] for _ in range(x_lim)] for _ in range(y_lim)]
    q = deque()
    q.append((0, 0, 1, 0))
    visited[0][0] = [True, True]
    while q:
        y, x, step, wall = q.popleft()
        # print(f"x={y}, y={x}, 현재 걸음 수={step}, 능력사용여부={True if wall==1 else False}, 현재 방문 상태={visited[y][x]}")
        if y == y_lim-1 and x == x_lim-1:
            return step
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < y_lim and 0 <= nx < x_lim:
                if board[ny][nx] == 0 and wall == 0 and not visited[ny][nx][0]:
                    q.append((ny, nx, step+1, wall))
                    visited[ny][nx][0] = True
                elif board[ny][nx] == 0 and wall == 1 and not visited[ny][nx][1]:
                    q.append((ny, nx, step+1, wall))
                    visited[ny][nx][1] = True
                elif board[ny][nx] == 1 and wall == 0 and not visited[ny][nx][1]:
                    q.append((ny, nx, step+1, 1))
                    visited[ny][nx][1] = True
    return -1

board = []
N, M = map(int, input().split())
for _ in range(N):
    board.append(list(map(int,list(sys.stdin.readline().rstrip()))))
print(bfs2(board))