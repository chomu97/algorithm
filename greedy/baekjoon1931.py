import sys

n = int(input())
times = []
for _ in range(n):
    times.append(list(map(int,input().split())))
times.sort(key=lambda x: (x[0], x[1]))
min_end = sys.maxsize
cnt = 1
for time in times:
    if min_end > time[1]:
        min_end = time[1]
    else:
        if min_end <= time[0]:
            cnt += 1
            min_end = time[1]
print(cnt)