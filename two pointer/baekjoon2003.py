N,M=map(int,input().split(' '))
nums=list(map(int,input().split(' ')))
start,end=0,0
count=0
subsum=0
while end<N:
    if subsum>=M:
        if subsum==M:
            count += 1
        subsum-=nums[start]
        start+=1
    else:
        subsum += nums[end]
        end += 1
print(count)