from collections import defaultdict
import heapq

V, E = map(int,input().split())
K = int(input())
nodes = defaultdict(list)
visited = [False for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int,input().split())
    nodes[u].append((v, w))

def dijkstra(nodes, visited, start):
    heap = [(0, start)]
    dist = defaultdict(int) # dist에 들어가 있다면 이미 방문한 노드.
    while heap:
        weight, end = heapq.heappop(heap)
        if not visited[end]:
            dist[end] = weight
            visited[end] = True
            for e, w in nodes[end]:
                alt = weight + w
                heapq.heappush(heap, (alt, e))
    return dist

res = dijkstra(nodes,visited,K)
for i in range(1, V+1):
    pr = res.get(i)
    print(pr if pr is not None else "INF")