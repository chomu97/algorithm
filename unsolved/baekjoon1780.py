import sys
N=int(input())
totalpaper=list()
for _ in range(N):
    totalpaper.append(list(map(int,sys.stdin.readline().split(' '))))
print(paper)
result={
    'minus' :0,
    'zero' :0,
    'plus':0
}
def papercount(num: int,paper: list):
    for row in range(num):
        for col in range(num):


