# def dfs(grid,i,j):
#     if i<0 or i>=len(grid) or j<0 or j>=len(grid[0])\
#             or grid[i][j]!=1:
#         return
#     grid[i][j]=0
#     dx=[1,-1,0,0,1,1,-1,-1]
#     dy=[0,0,1,-1,1,-1,1,-1]
#     for idx in range(8):
#         dfs(grid,i+dx[idx],j+dy[idx])
def dfs(grid,i,j):
    stack=[(i,j)]
    while stack:
        v=stack.pop()
        if v[0]<0 or v[0]>=len(grid) or v[1]<0\
            or v[1]>=len(grid[0]) or grid[v[0]][v[1]]!=1:
            continue
        grid[v[0]][v[1]]=0
        dx=[1,-1,0,0,1,1,-1,-1]
        dy=[0,0,1,-1,1,-1,1,-1]
        for idx in range(8):
            stack.append((v[0]+dx[idx],v[1]+dy[idx]))

while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    grid=[]
    for i in range(h):
        grid.append(list(map(int,input().split())))
    count=0
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1:
                dfs(grid,i,j)
                count+=1
    print(count)

