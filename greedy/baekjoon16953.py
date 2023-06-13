n, m = map(int, input().split())
isok = True
count = 1
while m != n and m > n:
    if m % 10 == 1:
        m = (m-1)//10
    else:
        m /= 2
    count += 1
    if m != int(m) or m < n:
        isok = False

if isok:
    print(count)
else:
    print(-1)