from collections import defaultdict
import heapq, sys

"""
def is_cycle(a, b, connects, N):
    nodes = []
    visited = [False for _ in range(N+1)]
    visited[a] = True
    for n in connects[a]:
        nodes.append(n[0])
    while nodes:
        curr = nodes.pop()
        if curr == b:
            return True
        if not visited[curr]:
            for n in connects[curr]:
                nodes.append(n[0])
            visited[curr] = True
    return False

N = int(input())
M = int(input())
edges = []
connects = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    heapq.heappush(edges, (c, a, b))

while edges:
    weight, s, e = heapq.heappop(edges)
    if not (is_cycle(s, e, connects, N)):
        connects[s].append((e, weight))
        connects[e].append((s, weight))

ans = 0
for i in connects.values():
    for j in i:
        ans += j[1]

print(ans//2)




위는 틀림X
크루스칼 알고리즘으로 구현
"""

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
M = int(input())
edges = []
connects = 0
parent = [i for i in range(N+1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    heapq.heappush(edges, (c, a, b))

while edges:
    weight, a, b = heapq.heappop(edges)
    if find_parent(parent, a) != find_parent(parent, b):
        connects += weight
        union_parent(parent, a, b)
print(connects)