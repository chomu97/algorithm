def str2ord(word):
    return ord(word) - ord('a') + 1


r = 31
M = 1234567891
length = int(input())
plain_text = input()
hashed = 0
for i, v in enumerate(plain_text):
    hashed += (str2ord(v) * (r ** i)) % M
print(hashed % M)