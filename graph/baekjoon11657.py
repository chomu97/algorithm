N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
INF = int(1e9)
cities = [INF] * (N+1)


def bellman_ford(start):
    cities[start] = 0
    for i in range(N):
        for s, e, w in edges:
            if cities[s] != INF and cities[s] + w < cities[e]:
                cities[e] = cities[s] + w
                if i == N-1:
                    return True
    return False


if bellman_ford(1):
    print(-1)
else:
    for i in range(2, N+1):
        print(cities[i] if cities[i] != INF else -1)