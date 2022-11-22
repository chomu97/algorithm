n=int(input())
arr=list(map(int,input().split(' ')))
# result=arr[0]
# for i in range(1,n):
#     if arr[i]<0:
#         result=arr[i-1]
#     else:
#         sums=[sum(arr[j:i+1]) for j in range(i)]
#         result=max(re)sult,max(sums))
#         print(i,sums
subsum=[arr[0]]
for i in range(1,len(arr)):
    subsum.append(arr[i] + (subsum[i-1] if subsum[i-1]>0 else 0))
print(max(subsum))