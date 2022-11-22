def solution(s):
    answer=0
    for i in range(1, len(s) // 2):
        for slice in s:

    return answer


# 일단 시작부터 전체 문자열 개수 만큼 부분 문자열 개수 찾아야함

# 1개부터 시작해서 문자열의 반까지만 반복.
# 문자열 슬라이싱해서 리스트에 담는다? 아님 딕셔너리에 담는다?
# idea 1 : 튜플에 담아서 ('문자열', 개수 )  문자열이 앞과 같으면 개수+1
# idea 2 : 그냥 리스트에 담아놨다가 개수만 찾고 가져온다


