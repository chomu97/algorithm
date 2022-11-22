import sys


def solution(topping):
    answer = 0
    """
    unique_topping = 0
    if len(topping) == 1:
        return 0
    leftIdx = 0
    rightIdx = len(topping) - 1

    leftSet = set()
    rightSet = set()

    
    while leftIdx != rightIdx:
        if len(leftSet) == len(rightSet):
            leftIdx += 1
            if topping[leftIdx] not in leftSet:
                leftSet.add(topping[leftIdx])
                unique_topping += 1
                answer = 0
            else:
                answer += 1
        else:
            rightIdx -= 1
            if topping[rightIdx] not in rightSet:
                rightSet.add(topping[rightIdx])
                if len(leftSet) == len(rightSet):
                    answer += 1
    
    while leftIdx != rightIdx:
        if len(leftSet) == len(rightSet):
            answer += 1
        leftIdx += 1
        if topping[leftIdx] not in leftSet:
            leftSet.add(topping[leftIdx])
            unique_topping += 1
            answer = 0
            rightIdx -= 1
            rightSet.add(topping[rightIdx])
        else:
            answer += 1

        print(leftIdx, rightIdx, answer)
    return answer
    """
    if len(topping)==1:
        return 0
    leftdict = {}
    rightdict = {}
    leftset = set()
    rightset = set()
    for i,v in enumerate(topping):
        if v not in leftset:
            leftset.add(v)
            leftdict[len(leftset)] = i
    for i,v in enumerate(topping[::-1]):
        if v not in rightset:
            rightset.add(v)
            rightdict[len(rightset)] = i
    print(leftdict, rightdict)
    min_answer = sys.maxsize
    for key in leftdict.keys():
        leftover = len(topping) - leftdict[key] - rightdict[key] - 2
        if leftover == 0:
            min_answer = 1
        elif leftover > 0:
            ans = leftover + 1
            if min_answer > ans:
                min_answer = ans
        else:
            if leftdict[len(set(topping[:-rightdict[key]]))] + rightdict[len(set(topping[leftdict[key]:]))] + 2 > len(topping):
                min_answer = sys.maxsize
    return min_answer if min_answer != sys.maxsize else 0

from collections import Counter

def solution2(lst):
    c = Counter(lst)
    b = set()
    answer = 0;
    for i in lst:
        b.add(i)
        if c.get(i) > 1:
            c[i] = c.get(i) - 1
        else:
            c.pop(i)
        if(len(c.keys())== len(b)):
            answer += 1
    print(len(c.keys()))
    print("answer" + str(answer))


print(solution([1,1,1,2,1,1,1]))
print(solution([1,1,1,2,2,3,2,2,1,1,1]))
print(solution2([1,2,3,1,1,1,1,4]))
print(solution([1,2,1,1,1,1,1,4]))
print(solution([1]))
print(solution([1,2]))
print(solution([1,2,3,5,6]))
print("----------해결------------")


# think 1 : 투포인터
# 양끝에서 시작하는데 하나씩 증가/ 감소할때 set의 길이가 같으면 answer += 1
# 근데 토핑의 종류가 늘어나면 answer =0 으로 초기화

# think 2 : 집합 양끝에서
# 양끝에서 가져 갈 수 있는 토핑 개수의 최소 인덱스를 찾음
# 하나씩 겹쳤을 때 인덱스 합이 길이보다 작으면 성립. 길이보다 크기 전까지 감. 그때의 개수 반환. 만약 다 전체 길이보다 크면 0
# 개수를 반환하고 둘을 합쳐 남은 원소의 개수 +1 만큼 반환하면 됨. 둘이 같으면 1 반환
