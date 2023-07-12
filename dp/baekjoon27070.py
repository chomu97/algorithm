X, T, M, V, N = map(int, input().split())
products = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)]

lim = M * V * T
t0 = M * X
if lim < t0:
    print(-1)
else:
    knapsack = [[0] * (lim + 1 - t0) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, lim+1-t0):
            weight = products[i][0] * products[i][1]
            value = products[i][2]
            if j < weight:
                knapsack[i][j] = knapsack[i-1][j]
            else:
                knapsack[i][j] = max(knapsack[i-1][j], knapsack[i-1][j-weight] + value)
    print(knapsack[-1][-1])

