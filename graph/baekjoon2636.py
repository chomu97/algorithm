from collections import deque
h, w = map(int,input().split())
board = []
for _ in range(h):
    board.append(list(map(int, input().split())))

def bfs(board, cheeze):
    air = deque()
    while cheeze:
        y, x = cheeze.pop()
        board[y][x] = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    h, w = len(board), len(board[0])
    visited = [[False for _ in range(w)] for _ in range(h)]
    air.append((0, 0))
    visited[0][0] = True

    while air:
        y, x= air.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx]:
                if board[ny][nx] == 0:
                    air.append((ny, nx))
                    visited[ny][nx] = 1
                elif board[ny][nx] == 1:
                    cheeze.append((ny, nx))
                    visited[ny][nx] = 1
    return board, cheeze


cheeze = []
ans = 0

while sum(sum(b) for b in board) != len(cheeze):
    ans += 1
    board, cheeze = bfs(board, cheeze)
    print(board, cheeze)
print(ans)
print(len(cheeze))

