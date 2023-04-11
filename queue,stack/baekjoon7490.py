# def is_zero(nums):
#     calc = ['', '+', '-']
#     answer = 1
#     for idx, num in enumerate(nums):
#         if num == '0':
#             if idx == 0:
#                 answer = answer * 10 + idx + 2
#             else:
#                 if nums[idx-1] == '1':
#                     answer = answer - (idx+2)
#         elif num == '1':
#             answer += idx + 2
#         else:
#             answer -= idx + 2
#     return answer == 0


from collections import deque
def is_zero2(nums: str, n: int):
    numbers = list(range(1,n+1))
    queue = deque()
    answer = 0
    for idx, num in enumerate(nums):
        if num == '0':
            queue.append(queue.pop()*10 + numbers[idx])
        else:
            queue.append(numbers[idx])
    for idx, num in enumerate(nums):
        if num == '0':
            continue
        elif num == '1':
            answer += queue.popleft()
        else:
            answer -= queue.popleft()
    return answer == 0


def print_nums(nums) -> str:
    calc = [' ', '+', '-']
    prt = '1'
    for idx, num in enumerate(nums[1:]):
        prt += str(calc[int(num)]) + str(idx+2)
    return prt


def num2tri(num) -> str:
    if num < 3:
        return str(num)
    else:
        return num2tri(num//3) + str(num % 3)

N = int(input())
for n in range(N):
    M = int(input())
    for i in range(3 ** (M-1)):
        nums = num2tri(i)
        nums = '1' + nums.rjust(M-1, '0')
        if is_zero2(nums, M):
            print(print_nums(nums))
    if n != N-1:
        print()