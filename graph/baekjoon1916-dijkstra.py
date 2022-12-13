from collections import defaultdict
import heapq

N = int(input())
M = int(input())
nodes = defaultdict(list)
visited = [False for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    nodes[s].append((e, w))
start, end = map(int, input().split())

def dijkstra(graph, visited, start, end):
    dist = defaultdict(int)
    heap = [(0, start)] # time, node 순으로 입력
    while heap:
        time, node = heapq.heappop(heap) # time이 작은 순서대로 pop
        if not visited[node]:
            dist[node] = time
            visited[node] = True
            for e, w in graph[node]:
                alt = time + w
                heapq.heappush(heap, (alt, e))
    return dist[end]

print(dijkstra(nodes, visited, start, end))