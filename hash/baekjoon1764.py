dud,bo=map(int,input().split())
dudli=dict()
result=[]
for _ in range(dud):
    dudli[input()]=0
for _ in range(bo):
    boword=input()
    if boword in dudli:
        result.append(boword)
result.sort()
print(len(result))
print('\n'.join(result))