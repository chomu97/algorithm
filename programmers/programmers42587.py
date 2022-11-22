import collections
def solution(priorities, location):
    answer = 0
    q = collections.deque(priorities)
    while True:
        prior = q.popleft()
        location -= 1
        if not q or (location == -1 and prior >= max(q)):
            break

        if prior >= max(q):
            answer += 1
        elif location == -1 and prior < max(q):
            q.append(prior)
            location += len(q)
        else:
            q.append(prior)
    return answer + 1

# 다른 사람의 풀이
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

def solution(priorities, location):
    answer = 0
    from collections import deque

    d = deque([(v,i) for i,v in enumerate(priorities)])

    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer

print(solution([2, 1, 3, 2], 3))
print(solution([1,1,9,1,1,1], 0))
