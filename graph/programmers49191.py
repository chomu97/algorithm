from collections import defaultdict


def dfs(graph, s, wl, n):
    stack = [i for i in graph[s]]
    discovered = [0 for _ in range(n+1)]
    discovered[s] = 1
    while stack:
        winner = stack.pop()
        if not discovered[winner]:
            discovered[winner] = 1
            wl[winner][0] += 1
            wl[s][1] += 1
            for loser in graph[winner]:
                stack.append(loser)
    return wl


def solution(n, results):
    answer = 0
    graph = defaultdict(list)
    win_lose = defaultdict(lambda: [0,0])
    for win, lose in results:
        graph[lose].append(win)
    for i in range(1, n+1):
        win_lose = dfs(graph, i, win_lose, n)

    for v in win_lose.values():
        answer += 1 if sum(v) == n-1 else 0
    return answer

# 경기 결과 모두 추가해둠.
# 한명씩 보면서 경기 결과를 유추할 수 있으면 모두 추가해둠.
# 한명씩 돌면서 경기 결과의 합이 인원수 - 1과 같은 경우 정확한 순위 매기기 가능.

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))