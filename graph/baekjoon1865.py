import sys

def bellman_ford(graph: list, start: int, nodes: int, dist):
    for i in range(nodes):
        for s, e, w in graph:
            if dist[s] != INF and dist[s] + w < dist[e]:
                dist[e] = dist[s] + w
                if i == N-1:
                    return True
    return False


N = int(input())
INF = 10 ** 9
input = sys.stdin.readline
for _ in range(N):
    N, M, W = map(int, input().split())
    graph = []

    for _ in range(M):
        s, e, t = map(int, input().split())
        graph.append((s, e, t))
        graph.append((e, s, t))

    for _ in range(W):
        s, e, t = map(int, input().split())
        t = -t
        graph.append((s, e, t))

    distance = [0] * (N+1) # 0으로 거리를 초기화하여 모든 정점이 시작 노드인 것 처럼 생각.
    print("YES" if bellman_ford(graph, 1, N, distance) else "NO")
    # for i in range(1, N+1):
    #     distance = [0] * (N + 1)
    #     if bellman_ford(graph, i, N, distance):
    #         print("YES")
    #         break
    # else:
    #     print("NO")
