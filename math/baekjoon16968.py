form = list(input())
res = 10 if form[0] == 'd' else 26
num = 0
for i in range(1,len(form)):
    if form[i] =='c':
        num = 26
    else:
        num = 10
    if form[i] == form[i-1]:
        num -= 1
    res *= num
print(res)