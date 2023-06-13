from collections import Counter
n, m = map(int, input().split())
number_list = list(map(int, input().split()))
cnts = Counter(number_list)


def dfs(numbers: list, count: Counter):
    if len(numbers) == m:
        print(' '.join(map(str, numbers)))
        return
    else:
        for i, c in sorted(count.items()):
            if c > 0:
                count2 = Counter(count)
                count2[i] -= 1
                dfs(numbers + [i], count2)

for i, c in sorted(cnts.items()):
    temp = Counter(cnts)
    temp[i] -= 1
    dfs([i], temp)