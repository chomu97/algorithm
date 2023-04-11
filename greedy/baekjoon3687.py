def find_min(n: int, answer: str) -> str:
    nums = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    while n > 0:
        if n < 8:
            # 맨 앞자리는 앞에서 부터 찾는게 최소
            # 6이라면 0을 반환할수 있으므로 예외처리
            return answer + str(nums[1:].index(n) + 1)
        elif n == 8:
            return answer + '01' # 고정
        elif n == 10:
            return answer + '32'
        elif n == 11:
            return answer + '02'
        else: # 중간의 경우는 성냥을 많이 쓰도록 가장 큰 7(8)을 빼 나가면 됨
            return find_min(n - 7, answer + '8')

# error : 10, 11, 17 ...
def find_min(n):
    nums = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    dp = [9, 9, 1, 7, 4, 2, 6, 8]
    if n < 8:
        asdf = [1, 7, 4, 2, 0, 8]
        return dp[n]
    else:
        for i in range(8, n + 1):
            dp.append(min(dp[i-2]*10+1, dp[i-5]*10+2, dp[i-4]*10+4, dp[i-6]*10+0, dp[i-3]*10+7, dp[i-7]*10+8))
        return dp[-1]

def find_max(n: int, answer: str) -> str:
    nums = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    while n > 0:
        if n == 3:
            return answer + '7'
        elif n == 2:
            return answer + '1'
        else: # 성냥을 가장 적게 사용하는 1을 계속 이어붙여 자릿수 크게.
            return find_max(n - 2, answer + '1')


N = int(input())
for _ in range(N):
    M = int(input())
    print(find_min(M), find_max(M, '')[::-1])