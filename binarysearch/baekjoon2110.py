def binary_search(houses, c):
    left = 0
    right = houses[-1] - houses[0] + 1
    mid = (left + right) // 2
    while left <= right:
        # if houses[-1] - houses[0] < mid:
        #     right = mid
        #     mid = (left + right) // 2
        # else:
            if install(houses, mid, c):
                left = mid + 1
                mid = (left + right) // 2
            else:
                right = mid - 1
                mid = (left + right) // 2
    return mid


def install(houses, mid, c):
    for idx, h in enumerate(houses):
        if idx == 0:
            c -= 1
            curr = h
        else:
            if h - curr >= mid:
                c -= 1
                curr = h
    return c <= 0

import sys
N, C = map(int, sys.stdin.readline().split())
houses = []
for _ in range(N):
    houses.append(int(sys.stdin.readline()))
houses.sort()

print(binary_search(houses, C))