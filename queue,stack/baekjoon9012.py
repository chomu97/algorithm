N = int(input())
for _ in range(N):
    stack = []
    ps = input()
    for w in ps:
        if not stack:
            stack.append(w)
        else:
            if stack[-1] == '(' and w == ')':
                stack.pop()
            else:
                stack.append(w)
    ans = 'NO' if stack else 'YES'
    print(ans)