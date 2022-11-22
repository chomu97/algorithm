num = int(input())
input_list = list(map(int,input().split()))
max_dp = max(input_list)
answer = list()
dp = [False, True, False, True]
if max_dp < 4:
    for i in input_list:
        answer.append(dp[i])
else:
    for i in range(4,max_dp+1):
        dp.append(False if dp[i-1] and dp[i-3] else True)
    for i in input_list:
        answer.append(dp[i])

goormy_wins = sum(answer)
friend_wins = num - goormy_wins
print( "tie" if goormy_wins == friend_wins else max(goormy_wins,friend_wins) )