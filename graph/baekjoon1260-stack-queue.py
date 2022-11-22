def dfs(graph, v):
    stack = []
    discovered = [v]
    for snode, enode in graph:
        if snode == v:
            stack.append(enode)
    while stack:
        node = stack.pop()
        if node not in discovered:
            discovered.append(node)
            for snode, enode in graph:
                if snode == node:
                    stack.append(enode)
    return discovered

def bfs(graph, v):
    queue = []
    discovered = [v]
    for snode, enode in graph:
        if snode == v:
            queue.append(enode)
    while queue:
        node = queue.pop(0)
        if node not in discovered:
            discovered.append(node)
            for snode, enode in graph:
                if snode == node:
                    queue.append(enode)
    return discovered


def dfs_recursive(graph, v, discovered=[]):
    discovered.append(v)
    for snode, enode in graph:
        if snode == v:
            if enode not in discovered:
                print(enode)
                discovered = dfs_recursive(graph, enode, discovered)
    return discovered

N, M, V = map(int, input().split())
graph = []
for i in range(M):
    s, e = map(int, input().split())
    graph.append((s, e))
    graph.append((e, s))
graph = list(set(graph))
dfs_graph = sorted(graph, key=lambda x: x[1], reverse=True)
bfs_graph = sorted(graph, key=lambda x: x[1], reverse=False)
print(bfs_graph)
# ans1 = list(map(str, dfs(dfs_graph, V)))
ans1 = list(map(str, dfs_recursive(bfs_graph, V)))
print(dfs_recursive(dfs_graph, V))
ans2 = list(map(str,bfs(bfs_graph, V)))
print(' '.join(ans1))
print(' '.join(ans2))

