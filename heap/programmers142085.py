import heapq

def solution(n, k, enemy):
    answer = 0
    defend = []
    min_defend = 10000001
    for i, v in enumerate(enemy):
        if len(defend) < k:
            if min_defend > v:
                min_defend = v
            heapq.heappush(defend, v)
        else:
            if min_defend < v:
                minus = heapq.heappop(defend)
                heapq.heappush(defend, v)
                min_defend = defend[0]
                n -= minus
            else:
                n -= v
            if n < 0:
                answer = i
                break
    if n>=0:
        answer = len(enemy)
    return answer

# 이렇게 간결하게 할 수 있음..
# import heapq as hq
# def solution(n, k, enemy):
#     q = enemy[:k]
#     hq.heapify(q) # 위에서 K보다 작은 경우 append했는데 이렇게 슬라이싱해서 heapify연산으로 힙으로 변환 가능.
#     for idx in range(k,len(enemy)):
#         n -= hq.heappushpop(q,enemy[idx]) # push,pop 연산을 동시에 함. 이게 각각 하는것 보다 빠르다고 document에 나와있음.
#         if n < 0:
#             return idx
#     return len(enemy)