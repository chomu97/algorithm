import sys
input = sys.stdin.readline
N, M = map(int,input().split())
products = [[0,0]]

temp = [list(map(int, input().split())) for _ in range(N)]


# 핵심 : 0-1 knapsack 문제로 환원해야 하는데 이 때 한 물건을 모두 1개씩으로 나누는 것이 아니라 1+2+4+8+ ... + 나머지 로 나누는 것이 핵심.
for v, c, k in temp:
    start = 1
    while k >= start:
        products.append([v*start, c*start])
        k -= start
        start *= 2
    if k != 0:
        products.append([v*k, c*k])

knapsack = [[0] * (M+1) for _ in range(len(products))]

for i in range(1, len(products)):
    for j in range(1, M+1):
        weight = products[i][0]
        value = products[i][1]
        if j < weight:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(knapsack[i-1][j-weight] + value, knapsack[i-1][j])

print(knapsack[-1][-1])

