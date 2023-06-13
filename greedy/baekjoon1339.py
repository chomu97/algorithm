from collections import defaultdict
N = int(input())
words = [input() for _ in range(N)]
words.sort(key=lambda x: len(x), reverse=True)
mapping = defaultdict(int)
for word in words:
    square = 10 ** (len(word) - 1)
    for w in word:
        mapping[w] += square
        square //= 10

mapping2 = []
for alpha, val in mapping.items():
    mapping2.append((alpha, val))
mapping2.sort(key=lambda x: x[1], reverse=True)

num = '9'
mapping3 = []
for alpha, val in mapping2:
    mapping3.append((alpha, num))
    num = chr(ord(num) - 1)

answer = 0
for word in words:
    for m in mapping3:
        word = word.replace(*m)
    answer += int(word)
print(answer)

# # 주니온 TV 풀이
# N = int(input())
# words = [input() for _ in range(N)]
# T = [0] * 26
# for word in words:
#     for i in range(len(word)):
#         T[ord(word[i]) - ord('A')] += 10 ** i
# T.sort(reverse=True)
# S = 0
# for i in range(10):
#     S += T[i] * (9 - i)
# print(S)