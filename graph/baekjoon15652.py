n, m = map(int, input().split())

def dfs(numbers: list):
    if len(numbers) >= 2 and numbers[-1] < numbers[-2]:
        return
    if len(numbers) == m:
        print(' '.join(map(str, numbers)))
        return
    else:
        for i in range(1, n + 1):
            dfs(numbers + [i])

for i in range(1, n+1):
    dfs([i])
