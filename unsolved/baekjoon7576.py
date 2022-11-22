from queue import PriorityQueue
col,row=map(int,input().split(' '))
box=[]
checkbox=[]
queue=PriorityQueue()
temp=PriorityQueue()
for i in range(row):
    box.append([])
    checkbox.append([])
    tomato_row=list(map(int, input().split(' ')))
    for j in range(col):
        box[i].append(tomato_row[j])
        if tomato_row[j]==1 or tomato_row[j]==0:
            checkbox[i].append(0)
        else:
            checkbox[i].append(1)
        if tomato_row[j]==1:
            queue.put((i,j))
cnt=0
while True:
    if queue.empty() and temp.empty():
        cnt-=1
        if any(0 in line for line in checkbox):
            cnt=-1
        break
    if queue.empty():
        cnt += 1
        queue=temp
        temp=PriorityQueue()
    start=queue.get()
    x,y=start[0],start[1]
    print(x,y,queue.queue)
    if checkbox[x][y] or box[x][y]==-1:
        continue
    else:
        if x==0: # first line
            if not checkbox[x+1][y]:
                temp.put((x+1,y))
                box[x][y]=cnt
        elif x==row-1: # last line
            if not checkbox[x - 1][y]:
                temp.put((x-1,y))
                box[x-1][y]=cnt
        else: # middle line
            if not checkbox[x - 1][y]:
                temp.put((x-1,y))
                box[x - 1][y] = cnt
            if not checkbox[x + 1][y]:
                temp.put((x+1,y))
                box[x+1][y]=cnt
        if y==0: # first line
            if not checkbox[x][y+1]:
                temp.put((x,y+1))
                box[x][y+1]=cnt
        elif y==col-1: # last line
            if not checkbox[x][y-1]:
                temp.put((x,y-1))
                box[x][y-1]=cnt
        else: # middle line
            if not checkbox[x][y-1]:
                temp.put((x,y-1))
                box[x][y - 1] = cnt
            if not checkbox[x][y+1]:
                temp.put((x,y+1))
                box[x][y+1]=cnt
    checkbox[x][y] = 1
print(cnt)
