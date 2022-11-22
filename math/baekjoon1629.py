num1,exp1,modulo1=map(int,input().split(' '))
res1=num1
def power(num,exp,modulo):
    if exp==1:
        return num%modulo
    res=power(num,exp//2,modulo)
    if exp%2==0:
        res= (res*res) %modulo
    else:
        res= (res * res %modulo)*num %modulo
    return res

# while exp>1:
#     print(res,exp)
#     if exp%2==0:
#         exp//=2
#         res*=res
#     else:
#         exp-=1
#         res*=num
print(power(num1,exp1,modulo1))
# print(pow(num,exp,modulo))
