# n = int(input())
# trump = list(map(int, input().split()))
# m = int(input())
# q_lst = list(map(int, input().split()))
# trump.sort()
# res=[]
#
# for i in q_lst:
#   left = 0
#   right = len(trump)-1
#   cnt = 0 # 추가된 라인
#   find = True # 추가된 라인
#   while find == True:
#     while left<=right: # 강의영상에 본대로 이분탐색 시작
#       mid = (left+right)//2
#       if trump[mid] == i:
#         # while trump[mid]==i: # 찾고자 하는 숫자 찾았으면 동일한 값이 있는 제일 왼쪽 인덱스로 이동
#         #   idx=mid
#         #   mid -= 1
#         cnt += 1
#         # while trump[idx]==trump[idx+1]: # 다시 오른쪽으로 가면서 개수 카운트
#         #   cnt+=1
#         #   idx+=1
#         #   if idx+1 == len(trump)-1: # out of range 오류 안나도록.. 이런 조건을 줌..
#         #     cnt+=1
#         #     break
#         # res.append(cnt)
#         print('빼기전',trump, mid)
#         trump.pop(mid) # 추가된 라인
#
#         break
#       elif trump[mid] < i:
#         left = mid+1
#       elif trump[mid] > i:
#         right = mid-1
#     # if trump[idx] != i: # 찾고자 하는 숫자가 없으면 0을 append
#     #   res.append(0)
#     # ------ 추가
#     if mid == len(trump):
#       mid -= 2
#     elif mid != 0:
#       mid -= 1
#     print('빼고난후', trump, mid)
#     if not trump or (trump[mid] != i and trump[mid+1] != i):
#       find = False # 조건 변경. 찾고자 하는 숫자가 없으면 find를 False로 변경
#   res.append(str(cnt))
#
# # for i in res:
# #   print(i,end=" ")
# print(' '.join(res))


n = int(input())
trump = list(map(int, input().split()))
m = int(input())
q_lst = list(map(int, input().split()))
trump.sort()
res=[]
for i in q_lst:
  left = 0
  right = len(trump)-1
  while left<=right: # 이분탐색 시작
    mid = (left+right)//2
    tmp=mid
    if trump[mid] == i: # mid 찾았으면 ,
      cnt=1
      while trump[mid-1] == i: # 왼쪽으로 가면서 cnt+=1
        mid -= 1
        cnt += 1
      mid = tmp
      while trump[mid+1] == i: # 오른쪽으로 가면서 cnt+=1
        mid += 1
        cnt += 1
        if mid ==len(trump)-1: # 오른쪽 끝이면 break.
          break
      res.append(str(cnt))
      break
    elif trump[mid] < i:
      left = mid+1
    elif trump[mid] > i:
      right = mid-1
  if trump[tmp]!=i: #  없으면 0 append
    res.append(0)
print(' '.join(res))