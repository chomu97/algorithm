from collections import Counter
from itertools import combinations
def solution(orders, course):
    answer = []
    for c in course:
        cnt = Counter()
        for order in orders:
            cnt.update(combinations(sorted(order),c))
        maxval = cnt.most_common()[0][1] if cnt.most_common() else 0
        answer += ["".join(k) for k, v in cnt.items() if maxval == v and v > 1]
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))