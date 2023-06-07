N, M = map(int, input().split())
board = [[0] * (M+2)]
for _ in range(N):
    board.append([0] + list(map(int,input().split())) + [0])
board.append([0] * (M+2))


def check(row, col, board):
    value = 0
    # 1*4 block
    if col <= len(board[0]) - 4:
        value = sum(board[row][col + dx] for dx in range(4))
    # 4*1 block
    if row <= len(board) - 4:
        value = max(value, sum(board[row + dy][col] for dy in range(4)))

    # 2*2 block
    value = max(value, sum([board[row][col], board[row+1][col], board[row][col+1], board[row+1][col+1]]))

    # L block
    dydx = [
        [(sum, [[-1, 0], [0, 0], [1, 0]]), (max, [[-1, -1], [-1, 1], [1, -1], [1, 1]])],
        [(sum, [[0, -1], [0, 0], [0, 1]]), (max, [[-1, -1], [-1, 1], [1, -1], [1, 1]])]
    ]
    for d in dydx:
        temp_sum = d[0][0](board[row + dy][col + dx] for dy, dx in d[0][1])
        temp_max = d[1][0](board[row + dy][col + dx] for dy, dx in d[1][1])
        value = max(value, temp_sum + temp_max)

    # T block
    dydx = [[[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]], [[-1, 0], [1, 0], [0, -1], [0, 1]]]
    temp_sum = sum(board[row + dy][col + dx] for dy, dx in dydx[0])
    temp_min = min(board[row + dy][col + dx] for dy, dx in dydx[1])
    value = max(value, temp_sum - temp_min)

    # z block
    dydx = [
        [[[0, 0], [-1, 0], [0, -1]], [[-1, 1], [1, -1]]],
        [[[0, 0], [-1, 0], [0, 1]], [[-1, -1], [1, 1]]]
    ]
    temp_val = 0
    for d in dydx:
        temp_sum = sum(board[row + dy][col + dx] for dy, dx in d[0])
        temp_max = max(board[row + dy][col + dx] for dy, dx in d[1])
        temp_val = max(temp_val, temp_sum + temp_max)
    value = max(value, temp_val)

    return value


max_value = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        max_value = max(max_value, check(i, j, board))
print(max_value)

"""
5 5
1 1 1 1 1
1 1 1 1 1
1 1 9 9 1
1 1 8 9 9 
1 1 1 1 1

답 36
"""