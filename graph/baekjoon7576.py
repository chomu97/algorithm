from collections import deque
N, M = map(int, input().split())
box = []
tomatoes = deque()
for row in range(M):
    box.append([])
    for col, t in enumerate(list(map(int, input().split()))):
        box[row].append(t)
        if t == 1:
            tomatoes.append((row, col))
d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
while tomatoes:
    x, y = tomatoes.popleft()
    for dx, dy in d:
        nrow = x + dx
        ncol = y + dy
        if (0 <= nrow <= M-1) and (0<= ncol <= N-1):
            if box[nrow][ncol] == 0:
                box[nrow][ncol] = box[x][y] + 1
                tomatoes.append((nrow, ncol))
            elif box[nrow][ncol] >= 0:
                box[nrow][ncol] = min(box[x][y] + 1, box[nrow][ncol])
if any(0 in b for b in box):
    print(-1)
else:
    print(max(max(b) for b in box) - 1)