def bfs(board, s):
    queue = [s]
    board[s[0]][s[1]] = 0
    diff = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    discovered = []
    cnt = 0
    while queue:
        new = queue.pop(0)
        if (N-1, M-1) in queue:
            break
        cnt += 1
        for drow, dcol in diff:
            row, col = new
            row += drow
            col += dcol
            if (0 <= row <= N-1) and (0 <= col <= M-1):
                if board[row][col] != 0 and (row, col) not in discovered:
                    queue.append((row, col))
                    discovered.append((row, col))
                    board[row][col] = 0
        print(new)
    return cnt


N, M = map(int, input().split())
board = []
for i in range(N):
    row = input()
    board.append([])
    for j in row:
        board[i].append(int(j))
print(bfs(board, (0, 0)))