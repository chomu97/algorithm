def is_prime(N):
    if N != 2 and  N % 2 == 0:
        return False
    i = 3
    for i in range(i, int(N**0.5) + 1, 2):
        if N % i == 0:
            return False
    return True


def calc(A,B,goals):
    A_in = goals[0]
    A_in_var = 1
    for i in range(18, 18 - goals[0], -1):
        A_in_var *= i/(i-(18-goals[0]))
    B_in = goals[1]
    B_in_var = 1
    for i in range(18, 18- goals[1], -1):
        B_in_var *= i/(i-(18-goals[1]))
    A_out = 18 - goals[0]
    B_out = 18 - goals[1]
    return ((1-A/100)**A_out)*((A/100)**A_in)*A_in_var*((1-B/100)**B_out)*((B/100)**B_in)*B_in_var

A = int(input())
B = int(input())
rounds = 18
goals = []
primes = []
for round in range(2, rounds+1):
    if is_prime(round):
        primes.append(round)
for i in range(19):
    for j in range(i,19):
        if i in primes or j in primes:
            goals.append((i, j))
sums = 0
for goal in goals:
    if goal[0] == goal[1]:
        sums += calc(A, B, goal)
    else:
        sums += calc(A, B, goal)
        sums += calc(B, A, goal)
print(sums)

# 0:0 ~ 18:18 경우 중 적어도 1개가 소수인 부분 탐색. ( 모두 소수가 아닌 부분을 제외하고 모두 다임 )
# 해당 경우들에 대해 확률 계산
# 50,50 이면 4가지 경우의수. [0,0] [0,1] [1,0] [1,1]
# 0~5분까지 10000경기를 한다고 생각하면 2500경기씩 해당 경우의수에 들어간다.
# 5~10분까지 10000경기를 한다고 생각하면 다시 해당 경우의수 만큼 나뉜다.
# 0:0으로 끝나는 확률은 1 * (1 - A/100)^45 * (1 - B/100)^45
# 0:1 또는 1:0으로 끝나는 확률은 {(1 - A/100)^45 * (1 - B/100)^ 44 * (B/100)^1 * 45 + (1-A/100)^44*(A/100)^1 * 45 *(1-B/100)^45}
# 0:2, 2:0으로 끝나는 확률은


3687

