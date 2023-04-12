import sys
import heapq
N = int(input())
meeting = []
room = []
for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    meeting.append([s, e])
meeting.sort(key=lambda x: x[0])
for s, e in meeting:
    if not room:
        heapq.heappush(room, e)
    else:
        if room[0] <= s:
            heapq.heappushpop(room, e)
        else:
            heapq.heappush(room, e)
print(len(room))