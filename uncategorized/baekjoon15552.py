import sys
N = int(input())
for _ in range(N):
    print(sum(list(map(int, sys.stdin.readline().rstrip().split()))))