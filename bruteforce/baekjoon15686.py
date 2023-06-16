from itertools import combinations

n, m = map(int, input().split())

house = []
chicken = []

for i in range(n):
    lst = list(map(int, input().split()))
    for j, v in enumerate(lst):
        if v == 1:
            house.append((i, j))
        elif v == 2:
            chicken.append((i, j))


def get_chicken_dist(house, chicken):
    chicken_dist = [100] * len(house)
    for i, h in enumerate(house):
        chicken_dist[i] = min(abs(c[0] - h[0]) + abs(c[1] - h[1]) for c in chicken)
    return sum(chicken_dist)


comb = combinations(chicken, m)

dist = 1e9
for c in comb:
    temp = get_chicken_dist(house, c)
    if dist > temp:
        dist = temp
print(dist)
