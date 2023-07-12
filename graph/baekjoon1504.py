import sys
import heapq as hq
input = sys.stdin.readline
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


v1, v2 = map(int, input().split())
def dijkstra(start):
    h = [(0, start)]
    visited = [False for _ in range(N+1)]
    dist = [0] * (N+1)
    while h:
        time, node = hq.heappop(h)
        if not visited[node]:
            dist[node] = time
            visited[node] = True
            for e, w in graph[node]:
                hq.heappush(h, (time + w, e))
    return dist



d1 = dijkstra(1)
d2 = dijkstra(v1)
d3 = dijkstra(v2)

c1 = all([d1[v1], d2[v2], d3[N]])
c2 = all([d1[v2], d3[v1], d2[N]])
if v1 == 1 and v2 == N:
    print(d1[N] if d1[N] else -1)
elif not c1 and not c2:
    print(-1)
elif not c1:
    print(d1[v2] + d3[v1] + d2[N])
elif not c2:
    print(d1[v1] + d2[v2] + d3[N])
else:
    print(min(d1[v1] + d2[v2] + d3[N], d1[v2] + d3[v1] + d2[N]))