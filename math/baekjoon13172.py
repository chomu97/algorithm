import sys

def get_modulo_inverse_elem(a:int, pw:int):
    if pw == 1:
        return a % 1000000007
    else:
        if pw % 2 == 0:
            return ((get_modulo_inverse_elem(a, pw//2) % 1000000007) ** 2 ) % 1000000007
        else:
            return (((get_modulo_inverse_elem(a, (pw-1)//2) % 1000000007)**2) % 1000000007  * a) % 1000000007

m = int(input())
pw = 1000000005
result = 0
for _ in range(m):
    n, s = map(int, input().split())
    if s % n != 0:
        a = get_modulo_inverse_elem(n, pw)
        result += (s * a)% 1000000007
        result %= 1000000007
    else:
        result += s // n
        result %= 1000000007
print(result)
