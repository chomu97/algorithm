def get_divisors(num):
    cnt = 0
    if int(num ** 0.5) ** 2 == num:
        cnt += 1
        end = int(num ** 0.5)
    else:
        end = int(num ** 0.5) + 1
    for i in range(1, end):
        if num % i == 0:
            cnt += 2
    return cnt
# 위의 함수는 사용했을 때 안됨. 이후에 왜 안됐는지 비교 필요. 일단 테스트케이스 9,10에서 시간초과.

def solution(e, starts):
    divisors_dp = [0]
    divisors_list = [0 for i in range(e + 1)]
    for i in range(2, e + 1):
        for j in range(1, min(e // i + 1, i)):
            divisors_list[i * j] += 2
    for i in range(1, int(e ** 0.5) + 1):
        divisors_list[i ** 2] += 1

    length = len(divisors_list) - 1
    for idx, value in enumerate(divisors_list[:0:-1]):
        divisors_dp.append(length - idx if divisors_list[divisors_dp[idx]] <= value else divisors_dp[idx])
    return [divisors_dp[length - s + 1] for s in starts]

print(solution(8,[1,3,7]))
print(solution(1,[1]))
print(solution(30,[1,3,7,25,30]))