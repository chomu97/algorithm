n, k = map(int, input().split())
words = list()
for _ in range(n):
    words.append(input())
words.sort(key= lambda x : (len(x),x))
print(words[k-1])