from collections import defaultdict, deque

def bfs(n, s, graph):
    queue = deque()
    queue.append((s, 0))
    discovered = [0 for _ in range(n+1)]
    result = [0 for _ in range(n+1)]
    while queue:
        node, h = queue.popleft()
        if not discovered[node]:
            discovered[node] = 1
            result[h] += 1
            for n in graph[node]:
                queue.append((n, h+1))
    for i in range(len(result)):
        if result[i] == 0:
            return result[i-1]


def solution(n, edge):
    graph = defaultdict(list)
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)
    return bfs(n, 1, graph)

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))