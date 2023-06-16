import sys
sys.setrecursionlimit(10**9)

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N):
    tmp = list(map(int, input().split()))[:-1]
    s = tmp[0]
    for i in range(1, len(tmp[1:]), 2):
        e = tmp[i]
        w = tmp[i+1]
        tree[s].append((e, w))

def dfs(s, weight):
    for e, w in tree[s]:
        if distance[e] == -1:
            distance[e] = w + weight
            dfs(e, w + weight)

distance = [-1] * (N + 1)
distance[1] = 0
dfs(1, 0)
start_index = distance.index(max(distance))
distance = [-1] * (N + 1)
distance[start_index] = 0
dfs(start_index, 0)
print(max(distance))