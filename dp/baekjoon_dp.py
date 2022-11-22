# #1463
# N=int(input())
# if N==1:
#     print(0)
# else:
#     dp=[0,0,1,1]
#     if N>=4:
#         for i in range(4,N+1):
#             check=[]
#             if i%2==0:
#                 check.append(dp[i//2]+1)
#             if i%3==0:
#                 check.append(dp[i//3]+1)
#             check.append(dp[i-1]+1)
#             dp.append(min(check))
#         print(dp[N])
#     else:
#         print(dp[N])
# #1003
# T=int(input())
# N=[]
# for _ in range(T):
#     N.append(int(input()))
# dp=[[1,0],[0,1]]
# if max(N)>1:
#     for i in range(2,max(N)+1):
#         dp.append([dp[i-2][0]+dp[i-1][0],dp[i-2][1]+dp[i-1][1]])
# for n in N:
#     print(str(dp[n][0])+' '+str(dp[n][1]))
#
# #2839
# import sys
# N=int(input())
# m=sys.maxsize
# dp=[m,m,m,1,m,1]
# if N>5:
#     for i in range(6,N+1):
#         dp.append(min(dp[i-3]+1,dp[i-5]+1))
# if dp[N]>=m:
#     print(-1)
# else:
#     print(dp[N])
# #1149
# N=int(input())
# R,G,B=map(int,input().split())
# dp=[R,G,B]
# for i in range(1,N):
#     R, G, B = map(int, input().split())
#     dp=[min(R+dp[1],R+dp[2]),min(G+dp[0],G+dp[2]),min(B+dp[0],B+dp[1])]
# print(min(dp))
#2579
N=int(input())
dp=[]
count=0
for i in range(N):
    score=int(input())
    if i>=1:
        if count==3:
            dp.append(dp[i-2]+score)
        else:
            dp.append(max(dp[i-1],dp[i-2])+score)
            if dp[i-1]>dp[i-2]:
                count+=1
            else:
                count=0
    else:
        dp.append(score)
        count+=1
print(dp[N-1])
# #11053
# N=int(input())
# A=list(map(int,input().split()))
# dp=[1]*N #dp[n]=n번째 수를 마지막으로 가지는 가장 긴 증가하는 부분수열의 count
# for i in range(1,N):
#     for j in range(i):
#         if A[j]<A[i]:
#             dp[i]=max(dp[i],dp[j]+1)
# print(max(dp))
# # 1932
# N=int(input())
# nums=[]
# for i in range(N):
#     nums.append(list(map(int, input().split())))
# dp=[[nums[0]]]
# for i in range(1,N):
#     dp.append([])
#     for j in range(len(nums[i-1])):
#         dp[i].append(max(dp[i-1][j]+nums[i][j],dp[i-1][j]+nums[i][j+1]))
#     print(dp)
# print(max(dp[N-1]))
