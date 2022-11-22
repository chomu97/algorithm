def solution(n, lost, reserve):
    c = [1] * (n+2)
    for i in lost:
        c[i] -= 1
    for i in reserve:
        c[i] += 1

    for i, v in enumerate(c): # backward
        if v == 0:
            if c[i+1] == 2 and c[i-1] == 2:
                c[i-1] -= 1
                c[i] += 1
            elif c[i-1] == 2:
                c[i-1] -= 1
                c[i] += 1
            elif c[i+1] == 2:
                c[i+1] -= 1
                c[i] += 1
    return n - c.count(0)

print(solution(10,[2,4],[3,5,6,7]))
print(solution(8, [1,3,5,7], [2,6,8]))