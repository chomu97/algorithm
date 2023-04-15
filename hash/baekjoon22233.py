import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
keywords = dict()
for _ in range(N):
    key = sys.stdin.readline().rstrip()
    keywords[key] = True
for _ in range(M):
    paragraph = sys.stdin.readline().rstrip().split(',')
    for i in paragraph:
        if i in keywords:
            keywords.pop(i)
    print(len(keywords))