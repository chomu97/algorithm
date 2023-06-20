from collections import deque
sik = input()
specials = []
result = ''

l1 = ['+', '-']
l2 = ['*', '/']

for i in sik:
    if ord("A") <= ord(i) <= ord("Z"):
        result += i
    else:
        if i in l2:
            while specials and specials[-1] in l2:
                result += specials.pop()
            specials.append(i)
        elif i in l1:
            while specials and (specials[-1] in l1 or specials[-1] in l2):
                result += specials.pop()
            specials.append(i)
        elif i == ')':
            while specials[-1] != '(':
                result += specials.pop()
            specials.pop()
        else:
            specials.append(i)
while specials:
    result += specials.pop()
print(result)