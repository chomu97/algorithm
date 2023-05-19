import heapq, sys
N = int(input())
h = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if n == 0 and not h:
        print(0)
    elif n == 0:
        print(heapq.heappop(h))
    else:
        heapq.heappush(h, n)