nums = []
for _ in range(9):
    nums.append(int(input()))
target = sum(nums) - 100
nums.sort()
del1 = 0
for i in range(8):
    for j in range(i+1,9):
        if nums[i] + nums[j] == target:
            del1, del2 = nums[i], nums[j]
            break
    if del1:
        break
nums.remove(del1)
nums.remove(del2)
print("\n".join([str(n) for n in nums[:7]]))