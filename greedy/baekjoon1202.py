import heapq, sys
N, K = map(int, input().split())
jewels = []
bags = []
for _ in range(N):
    M, V = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(jewels, (M, V))
for _ in range(K):
    C = int(sys.stdin.readline().rstrip())
    bags.append(C)

bags.sort()
answer = 0
temp_jewels = []
for b in bags:
    while jewels and b >= jewels[0][0]:
        heapq.heappush(temp_jewels, -heapq.heappop(jewels)[1])
    if temp_jewels:
        answer += -heapq.heappop(temp_jewels)
    elif not jewels:
        break
print(answer)