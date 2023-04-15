from collections import Counter
name = input()
name_count = Counter(name)

ans = ''
ans_len = 0
for i in sorted(name_count.keys()):
    while name_count[i] > 1:
        name_count[i] -= 2
        ans += i
        ans_len += 1
one_count = 0
for i in sorted(name_count.keys()):
    if name_count[i] == 1:
        one_count += 1
        ans += i
if one_count > 1:
    ans = "I'm Sorry Hansoo"
else:
    ans += ans[:ans_len][::-1]

print(ans)