def multify_matrix(a: list, b: list):
    res = []
    length = len(a)
    for i in range(length):
        res.append([])
        for j in range(length):
            temp = 0
            for k in range(length):
                temp += a[i][k] * b[k][j]
            res[i].append(temp % 1000)
    return res


def power_matrix(a: list, n: int):
    if n == 1:
        length = len(a)
        for i in range(length):
            for j in range(length):
                a[i][j] = a[i][j] % 1000
        return a
    if n % 2 == 0:
        lst = power_matrix(a, n//2)
        return multify_matrix(lst, lst)
    else:
        lst = power_matrix(a, (n-1)//2)
        return multify_matrix(multify_matrix(lst, lst), a)

n, b = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

result = power_matrix(arr, b)
for r in result:
    print(' '.join(map(str,r)))
