def bfs(board, s):
    queue = [s]
    board[s[0]][s[1]] = 0
    diff = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    result = [[0]*len(board[0]) for _ in range(len(board))]
    result[s[0]][s[1]] = 1
    while queue:
        new = queue.pop(0)
        if (N-1, M-1) in queue:
            break
        for drow, dcol in diff:
            row, col = new
            row += drow
            col += dcol
            if (0 <= row <= N-1) and (0 <= col <= M-1):
                if result[row][col] != 0:
                    result[row][col] = min(result[row][col], result[row-drow][col-dcol] + 1)
                if board[row][col] and result[row][col] == 0:
                    queue.append((row, col))
                    board[row][col] = 0
                    result[row][col] = result[row-drow][col-dcol] + 1
    return result[N-1][M-1]


N, M = map(int, input().split())
board = []
for i in range(N):
    row = input()
    board.append([])
    for j in row:
        board[i].append(int(j))
print(bfs(board, (0, 0)))