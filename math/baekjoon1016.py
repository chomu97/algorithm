def primes(N: int):
    prime = [False, False, True] + [True, False] * (N//2)
    answer = [2]
    for i in range(3, N+1):
        if prime[i]:
            answer.append(i)
            for j in range(i*2, N+1, i):
                prime[j] = False
    return answer

min_, max_ = map(int, input().split())

total = max_ - min_ + 1
prime = primes(1000000)
answer_set = set()
for p in prime:
    curr = p**2
    if curr > max_ or total < 0:
        break
    # total -= (max_//curr) - (min_ - 1)//curr # ==> 최소공배수를 고려 안했다는 문제가 있었음.
    # curr2 = max_ + 1 # ==> 굳이 스타트를 여기서 하지 않고 계산으로 초깃값 설정 가능.
    curr2 = (((min_ - 1)//curr) + 1) * curr
    while curr2 <= max_:
        answer_set.add(curr2)
        curr2 += curr
print(total - len(answer_set))