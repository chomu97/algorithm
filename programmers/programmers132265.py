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
print("----------??????------------")


# think 1 : ????????????
# ???????????? ??????????????? ????????? ??????/ ???????????? set??? ????????? ????????? answer += 1
# ?????? ????????? ????????? ???????????? answer =0 ?????? ?????????

# think 2 : ?????? ????????????
# ???????????? ?????? ??? ??? ?????? ?????? ????????? ?????? ???????????? ??????
# ????????? ????????? ??? ????????? ?????? ???????????? ????????? ??????. ???????????? ?????? ????????? ???. ????????? ?????? ??????. ?????? ??? ?????? ???????????? ?????? 0
# ????????? ???????????? ?????? ?????? ?????? ????????? ?????? +1 ?????? ???????????? ???. ?????? ????????? 1 ??????
