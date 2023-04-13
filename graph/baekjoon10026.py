def dfs(graph):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    y_lim = len(graph)
    x_lim = len(graph[0])
    count = 0
    stack = [(0,0)]
    while stack:
        while stack:
            y, x = stack.pop()
            curr = graph[y][x]
            graph[y][x] = 'K'
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < y_lim and 0 <= nx < x_lim:
                    if graph[ny][nx] != 'K' and graph[ny][nx] == curr:
                        stack.append((ny, nx))
        count += 1
        if count != 0:
            for y, g in enumerate(graph):
                for x, s in enumerate(g):
                    if s != 'K':
                        stack.append((y, x))
                        break
                else:
                    continue
                break
    return count


N = int(input())
pic = []
for _ in range(N):
    pic.append(input())

new_pic = [p.replace("G", "R") for p in pic]
pic = [list(p) for p in pic]
new_pic = [list(p) for p in new_pic]
print(dfs(pic))
print(dfs(new_pic))

