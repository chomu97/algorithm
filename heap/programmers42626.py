import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        min_scov = heapq.heappop(scoville)
        if min_scov >= K:
            break
        if not scoville:
            answer = -1
            break
        min2_scov = heapq.heappop(scoville)
        heapq.heappush(scoville, min_scov + min2_scov*2)
        answer += 1
    return answer

print(solution([1, 2, 3, 9, 10, 12],7))


# 마찬가지로 이런 식으로 pushpop을 이용하여 좀 더 효율성을 높일 수 있을 것 같음.
# def solution(scoville, K):
#     heapq.heapify(scoville)
#     size, cnt = len(scoville) - 1, 0
#     f = heapq.heappop(scoville)
#     while size > 0:
#         s = heapq.heappop(scoville)
#         f = heapq.heappushpop(scoville, f + s + s)
#         if f >= K:
#             return cnt + 1
#         cnt += 1
#         size -= 1
#     return -1