N, K = map(int, input().split())
products = [[0,0]]
knapsack = [[0] * (K+1) for _ in range(N+1)]
for i in range(N):
    w, v = map(int, input().split())
    products.append([w, v])
for i in range(1,N+1):
    for j in range(1,K+1):
        weight = products[i][0]
        value = products[i][1]
        if j < weight:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            # knapsack[i][j] = max( 바로 전의 가치, 바로 전에서 지금 무게의 물건을 넣었을 때 가치 )
            knapsack[i][j] = max(knapsack[i-1][j-weight] + value, knapsack[i-1][j])
print(knapsack)
print(knapsack[-1][-1])