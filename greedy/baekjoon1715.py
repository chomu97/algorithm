import heapq as hq

N = int(input())
cards = []
for _ in range(N):
    hq.heappush(cards, int(input()))
answer = 0
while len(cards) != 1:
    a = hq.heappop(cards)
    b = hq.heappop(cards)
    answer += a+b
    hq.heappush(cards, a + b)
print(answer)