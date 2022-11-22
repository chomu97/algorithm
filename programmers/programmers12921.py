# def solution(n):
#     answer = [2]
#     for i in range(3, n+1, 2):
#         answer.append(i)
#         if not isprime(i, answer):
#             answer.pop()
#     return len(answer)
#
#
# def isprime(n, prime):
#     cnt = 0
#     for i in prime[:n//2+1]:
#         cnt += 1 if n%i == 0 else 0
#     return cnt == 1
# def solution(n):
#     if n > 2:
#         answer = [0,0,1] + [1,0]*((n-1)//2)
#     else:
#         answer = [0,0,1]
#
#     for i in range(3,n+1,2):
#         if answer[i]==1:
#             for idx in range(i+i,n,i):
#                 answer[idx] = 0
#     return sum(answer)


def solution(n):
    if n > 2:
        answer = [0,0,1] + [1,0]*((n-1)//2)
    else:
        answer = [0,0,1]

    m = int(n**0.5)
    for i in range(3,m+1,2):
        if answer[i] == 1:
            for j in range(i+i,n+1,i):
                answer[j] = 0
    return sum(answer)

print(solution(121))
print(solution(11))
