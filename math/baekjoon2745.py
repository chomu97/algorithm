def eng2ord(str):
    return ord(str) - ord('A') + 10 if str.isalpha() else int(str)

def basen(num, base):
    base = int(base)
    result = 0
    for i, c in enumerate(num[::-1]):
        n = eng2ord(c)
        result += n * (base ** i)
    return result

n, b = input().split()
print(basen(n, b))