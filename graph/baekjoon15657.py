n, m = map(int, input().split())
number_list = list(map(int, input().split()))
number_list.sort()
def dfs(numbers: list):
    if len(numbers) >= 2 and numbers[-1] < numbers[-2]:
        return
    if len(numbers) == m:
        print(' '.join(map(str, [number_list[num] for num in numbers])))
        return
    else:
        for i in range(0, n):
            dfs(numbers + [i])

for i in range(0, n):
    dfs([i])
