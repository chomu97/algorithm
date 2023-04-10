from collections import defaultdict
T = int(input())
for _ in range(T):
    W = input()
    K = int(input())
    words = defaultdict(list)
    for idx, w in enumerate(W):
        words[w].append(idx)

    max_len = 0
    min_len = 10001
    for key, val in words.items():
        value_length = len(val)
        for i in range(value_length-K+1):
            result = val[i+K-1] - val[i] + 1
            if max_len < result:
                max_len = result
            if min_len > result:
                min_len = result
    if min_len == 10001:
        print(-1)
    else:
        print(min_len, max_len)