import collections
import heapq
N,M,X=map(int,input().split())
nodes=collections.defaultdict(list)
rev_nodes=collections.defaultdict(list)
for _ in range(M):
    s,e,t=map(int,input().split())
    nodes[s].append((e,t))
    rev_nodes[e].append((s,t))
def dijkstra(graph,start):
    Q=[(0,start)] # (time,node)
    dist=collections.defaultdict(int)
    while Q:
        time,node=heapq.heappop(Q)
        if node not in dist:
            dist[node]=time
            for v,w in graph[node]:
                alt=time+w
                heapq.heappush(Q,(alt,v))
    if len(dist)==N:
        return sorted(dist.items())
    return -1
go=dijkstra(nodes,X)
come=dijkstra(rev_nodes,X)
res=[]
for i in range(N):
    res.append(go[i][1]+come[i][1])
print(max(res))