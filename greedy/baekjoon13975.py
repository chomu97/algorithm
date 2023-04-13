import heapq
N = int(input())
for _ in range(N):
    K = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)
    ans = 0
    while files:
        a = heapq.heappop(files)
        if files:
            b = heapq.heappop(files)
            x = a + b
            ans += x
            heapq.heappush(files, x)
    print(ans)
