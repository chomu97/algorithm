T = int(input())
for _ in range(T):
    n = int(input())
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, input().split())))
    if n == 1:
        print(max(stickers[0][0], stickers[1][0]))
    else:
        dp = [[stickers[0][0], stickers[1][0]], [stickers[1][0] + stickers[0][1], stickers[0][0] + stickers[1][1]]]
        for i in range(2, n):
            dp.append([max(dp[-1][1], dp[-2][1], dp[-2][0]) + stickers[0][i], max(dp[-1][0], dp[-2][0], dp[-2][1]) + stickers[1][i]])
        print(max(dp[-1]))
