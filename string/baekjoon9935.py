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