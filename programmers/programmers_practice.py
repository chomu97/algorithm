#문자열 다루기 기본
def solution(s):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()

def solution2(n):
    answer = []
    cnt = 0
    for i in range(1,n+1,2):
        if isprime(i):
            cnt += 1
            answer.append(cnt)
    return answer[-1]
def isprime(n):
    cnt = 0
    for i in range(1,int(n**0.5)+1):
        cnt += 1 if n%i == 0 else 0
    return cnt == 1
print(solution2(100))
print(bool(0))