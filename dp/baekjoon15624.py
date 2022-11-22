m=1000000007
num=int(input())
fib=[0,1]
if num>1:
    for i in range(2,num+1):
        fib.append((fib[i-2]+fib[i-1])%m)
print(fib[num])