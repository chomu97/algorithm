from collections import Counter
N = int(input())
cards = Counter(map(int,input().split()))
M = int(input())
ans = list(map(int, input().split()))
res = []
for i in ans:
    res.append(str(cards[i]))
print(' '.join(res))