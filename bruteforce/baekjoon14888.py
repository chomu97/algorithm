from itertools import permutations
import sys
N = int(input())
nums = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())
max_num, min_num = -(sys.maxsize+1), sys.maxsize
max_num2, min_num2 = -(sys.maxsize+1), sys.maxsize
calc = ['p'] * plus + ['mi'] * minus + ['d'] * divide + ['mul'] * multiply
for lst in set(permutations(calc, plus+minus+divide+multiply)):
    result = nums[0]
    for i, v in enumerate(lst):
        if v == 'p':
            result += nums[i+1]
        elif v == 'mi':
            result -= nums[i+1]
        elif v == 'mul':
            result *= nums[i+1]
        else:
            if (result * nums[i + 1]) < 0:
                result *= -1
                result //= nums[i + 1]
                result *= -1
            else:
                result //= nums[i + 1]
    if max_num < result:
        max_num = result
    if min_num > result:
        min_num = result
print(max_num)
print(min_num)