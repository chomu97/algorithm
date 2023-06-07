N = int(input())
dp = []
for i in range(N):
    n1, n2, n3 = map(int, input().split())
    if i == 0:
        dp = [[n1, n2, n3], [n1, n2, n3]]
    else:
        min_temp = [0, 0, 0]
        # min
        for j in range(3):
            if j == 0:
                min_temp[j] = n1 + min(dp[0][0], dp[0][1])
            elif j == 1:
                min_temp[j] = n2 + min(dp[0])
            else:
                min_temp[j] = n3 + min(dp[0][1], dp[0][2])
        dp[0] = min_temp

        max_temp = [0, 0, 0]
        for j in range(3):
            if j == 0:
                max_temp[j] = n1 + max(dp[1][0], dp[1][1])
            elif j == 1:
                max_temp[j] = n2 + max(dp[1])
            else:
                max_temp[j] = n3 + max(dp[1][1], dp[1][2])
        dp[1] = max_temp

print(max(dp[1]), min(dp[0]))

# 주니온 TV 풀이

N = int(input())
dp = []
for i in range(N):
    n1, n2, n3 = map(int, input().split())
    min_temp = [0, 0, 0]
    # min
    p = min(dp[0][:2])
    q = min(dp[0][1:])
    # 이 두개의 값을 가지고 min(p, q)를 통해 dp 배열의 최솟값을 구할 수 있다.
    min_temp[0] = n1 + p
    min_temp[1] = n2 + min(p, q)
    min_temp[2] = n3 + q
    dp[0] = min_temp

    # max
    p = max(dp[1][:2])
    q = max(dp[1][1:])
    # 이 두개의 값을 가지고 min(p, q)를 통해 dp 배열의 최댓값을 구할 수 있다.
    max_temp[0] = n1 + p
    max_temp[1] = n2 + max(p, q)
    max_temp[2] = n3 + q
    dp[1] = max_temp

print(max(dp[1]), min(dp[0]))


#주니온 TV 숏코딩
M = m = [0]*3
n, *a = open(0)
for b in a:
    x, y, z = map(int, b.split())
M, m = ([x+f(v[:2]), y+f(v), z+f(v[1:])] for f, v in [(max, M), (min, m)])
print(max(M), min(m))