import heapq
def dijkstra(graph, visited, start):
    heap = [(0, start)]
    dist = defaultdict(int)
    while heap:
        weight, end = heapq.heappop(heap)
        if not visited[end]:
            dist[end] = weight
            visited[end] = True
            for k in graph[end].keys():
                alt = weight + graph[end][k]
                heapq.heappush(heap, (alt, k))
    return dist


from collections import defaultdict
N, M = map(int, input().split())
barn = defaultdict(dict)
visited = [False for _ in range(M+2)]
for _ in range(M):
    a, b, c = map(int, input().split())
    barn[a][b] = c if barn[a].get(b) is None or barn[a][b] > c else barn[a][b]
    barn[b][a] = c if barn[b].get(a) is None or barn[b][a] > c else barn[b][a]

print(dijkstra(barn, visited, 1)[N])