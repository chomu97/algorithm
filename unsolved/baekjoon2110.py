def check(house,mid):
    count=0

    if count>=c:
        return False
    else:
        return True

n,c=map(int,input().split())
house=[]
for _ in range(n):
    house.append(int(input()))
house.sort()
count=0
start=0
end=house[-1]-house[0]+1
while start+1<end:
    mid=(start+end)//2

    if count>=c:
        end=mid
    else:
        start=mid
    print(start)