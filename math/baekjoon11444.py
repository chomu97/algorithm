import sys
sys.setrecursionlimit(10 ** 9)
N = int(input())
fibo_dict = dict()

fibo_dict[1] = 1
fibo_dict[2] = 1

modulo = 1000000007


def fibo(n):
    if fibo_dict.get(n):
        return fibo_dict[n] % modulo
    if n % 2 == 0:
        fibo_dict[n] = (fibo(n//2) * fibo(n//2 - 1)) % modulo + (fibo(n//2 + 1) * fibo(n//2)) % modulo
    else:
        fibo_dict[n] = (fibo((n-1)//2) ** 2) % modulo + (fibo((n+1)//2) ** 2) % modulo
    return fibo_dict[n] % modulo


print(fibo(N))