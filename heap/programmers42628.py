import heapq

def solution(operations):
    h = []
    for op in operations:
        d, num = op.split()
        num = int(num)
        if d == "I":
            heapq.heappush(h, num)
        else:
            if h:
                if num == -1:
                    heapq.heappop(h)
                else:
                    h.pop() # 아래 주석처럼 h.pop()의 경우도 똑같이 max 값을 pop 하는 것이 아니기 때문에 틀렸다고 생각함.
    return [max(h), h[0]] if h else [0, 0]

# 힙 구조는 가장 우선순위가 높은 값이 먼저 pop 되는 것을 보장하는 자료구조이다.
# pq[0]가 가장 우선순위가 높은 값(가장 작은값)인 것은 맞지만, 나머지 값에 대한 정렬은 보장하지 않는다.
# 따라서 아래처럼 return을 하게 되면 틀린다.
# return [h[-1], h[0]] if h else [0, 0]

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I 10", "D 1", "I 1"]))