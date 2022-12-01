from collections import defaultdict
n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
tree_reverse = {}

stack = [1]
discovered = [0 for i in range(n+1)]
while stack:
    curr = stack.pop()
    discovered[curr] = 1
    for v in graph[curr]:
        if not discovered[v]:
            stack.append(v)
            tree_reverse[v] = curr

for i in range(2,n+1):
    print(tree_reverse[i])
# 딕셔너리로 풀어낼 지 고민.
# 아니면 리스트 안에 리스트를 넣어서?
# 연결 리스트로 풀어야 할듯? no
# 딕셔너리로 풀이. -> 인접행렬을 사용한다고 생각함.
# 추가할 때가 중요한데 1을 루트라고 했으니 1부터 탐색하면서 value에 이미 있는지 봐야한다. 있다면 그 아래에 추가해야한다.
# range(2,N+1) 까지 값을 찾는데
# 딕셔너리의 key들을 순회하면서 value에 있는지만 확인하면 그 key가 부모가된다.

# discovered 할 때 if v in discovered 가 아니라 -> if not discovered[v] 이런 식으로 O(1)에 가져올 수 있도록 변경.
# if v in discovered 는 최악의 경우 O(n)이 걸릴 수 있다.