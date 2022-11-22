import sys
k,n=input().split(' ')
lans=list()
for _ in range(int(k)):
    lans.append(int(sys.stdin.readline()))
start=1
end=max(lans)
mid=(start+end)//2
while end-start>=0:
    # if int(n)>end:
    #     end=0
    #     break
    cnt=0
    for lan in lans:
        cnt+=lan//mid
    if cnt>=int(n):
        start,mid=mid+1,(start+end)//2
    else:
        mid,end=(start+end)//2,mid-1
print(end)
