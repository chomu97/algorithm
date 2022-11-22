def check_chess(lst):
    check = [['WBWBWBWB', 'BWBWBWBW'] * 4, ['BWBWBWBW', 'WBWBWBWB'] * 4]
    cnt = [0,0]
    for idx,b in enumerate(check):
        for i in range(8):
            for j in range(8):
                if lst[i][j] == b[i][j]:
                    cnt[idx] += 1
    return min(cnt)

N, M = map(int, input().split())
board = []
min_cnt = N*M
for _ in range(N):
    board.append(input())
for row in range(N-7):
    for col in range(M-7):
        tmp = [i[col:col+8] for i in board[row:row+8]]
        tmp_cnt = check_chess(tmp)
        if min_cnt > tmp_cnt:
            min_cnt = tmp_cnt
print(min_cnt)
