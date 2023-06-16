from collections import deque

s, e = map(int, input().split())

def bfs(s: int, e: int):
    visited = [1e9] * 300000
    queue = deque([s])
    visited[s] = 0

    while queue:
        node = queue.popleft()
        visited.append(node)
        if node == e:
            return visited[e]
        if node * 2 < 300000 and visited[node * 2] > visited[node]:
            visited[node * 2] = visited[node]
            queue.appendleft(node * 2)
        if node + 1 < 300000 and visited[node + 1] > visited[node] + 1:
            visited[node + 1] = visited[node] + 1
            queue.append(node + 1)
        if node - 1 >= 0 and visited[node - 1] > visited[node] + 1:
            visited[node - 1] = visited[node] + 1
            queue.append(node - 1)

print(bfs(s, e))