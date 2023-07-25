n = int(input())
lst = list(map(int, input().split()))
lst2 = lst[::-1] # 뒤집은 수열을 추가하여 가장 긴 증가하는 부분 수열을 거꾸로 찾음.
dp = [1] * n # dp[n] = n번째 수를 가장 큰 수로 가지는 가장 긴 증가하는 부분 수열의 길이.
dp2 = [1] * n
answer = 0
for i in range(1, n):
    for j in range(i):
        if lst[j]<lst[i]:
            dp[i] = max(dp[i],dp[j]+1)
        if lst2[j]<lst2[i]:
            dp2[i] = max(dp2[i], dp2[j]+1)
dp2 = dp2[::-1] # 해당 뒤집은 수열의 dp 값을 다시 되돌려 가장 긴 감소하는 부분 수열로 만듬.
for i in range(n):
    if answer < dp[i] + dp2[i]:
        answer = dp[i] + dp2[i]
print(answer - 1)
