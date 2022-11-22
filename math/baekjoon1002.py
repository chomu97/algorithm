N=int(input())
for _ in range(N):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    distance=(((x1-x2)**2)+((y1-y2)**2))**0.5
    r=max(r1,r2)-min(r1,r2)
    if distance:
        if distance == r1+r2 or distance == r: print(1)
        elif r < distance < r1+r2: print(2)
        else: print(0)
    else:
        print(0) if r else print(-1)