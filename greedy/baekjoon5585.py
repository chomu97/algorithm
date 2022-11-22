change = 1000 - int(input())
count = 0
lst = [500, 100, 50, 10, 5, 1]
for coin in lst:
    while change >= coin:
        change -= coin
        count += 1
print(count)