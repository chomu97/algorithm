def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

while True:
    num = input()
    result = 0
    if num == "0":
        break
    for i in range(1, len(num) + 1):
        result += int(num[-i]) * factorial(i)
    print(result)