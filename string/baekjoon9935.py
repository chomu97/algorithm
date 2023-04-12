stack = []
words = input()
bomb = input()
bomb_length = len(bomb)
if bomb_length == 1:
    words = words.replace(bomb, '')
    print('FRULA' if not words else words)
else:
    for word in words:
        if stack:
            if ''.join(stack[-bomb_length+1:]) == bomb[:-1] and word == bomb[-1]:
                for _ in range(bomb_length-1):
                    stack.pop()
            else:
                stack.append(word)
        else:
            stack.append(word)
    print('FRULA' if not stack else ''.join(stack))

# bomb을 리스트에 넣으면 굳이 stack을 join시키지 않아도 됨.
# 9line 다음에서, 무조건 stack.append(word)를 한 다음에 11line 비교 구문을 stack[-bomb_length:] == bomb 하면 더 좋을 듯.