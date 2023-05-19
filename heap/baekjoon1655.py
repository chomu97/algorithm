import heapq
import sys
N = int(input())
answer = []
left_heap = [] # max heap
right_heap = [] # min heap
for i in range(N):
    n = int(sys.stdin.readline())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, (-n, n))
    else:
        heapq.heappush(right_heap, n)
    if right_heap and left_heap[0][1] > right_heap[0]:
        _, left = heapq.heappop(left_heap)
        right = heapq.heappop(right_heap)
        heapq.heappush(left_heap, (-right, right))
        heapq.heappush(right_heap, left)
    answer.append(left_heap[0][1])
for a in answer:
    print(a)