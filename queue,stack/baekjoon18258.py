import sys
from collections import deque
input= sys.stdin.readline
N=int(input())
queue=deque()
for _ in range(N):
    comm=input().rstrip()
    if comm[:4] == 'push':
        queue.append(int(comm.split()[1]))
    elif comm == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print('-1')
    elif comm == 'size':
        print(len(queue))
    elif comm == 'empty':
        if queue:
            print('0')
        else:
            print('1')
    elif comm == 'front':
        if queue:
            print(queue[0])
        else:
            print('-1')
    elif comm == 'back':
        if queue:
            print(queue[-1])
        else:
            print('-1')

