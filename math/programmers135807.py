def gcd(a, b):
    if not b:
        return a
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def gcd_all(*args):
    curr_gcd = None
    for i in args:
        curr_gcd = gcd(i, curr_gcd)
    return curr_gcd

def solution(arrayA, arrayB):
    tf_list = [True, True]
    gcd_list = [gcd_all(*arrayA), gcd_all(*arrayB)]

    for i in arrayB:
        if i % gcd_list[0] == 0:
            tf_list[0] = False
            break

    for i in arrayA:
        if i % gcd_list[1] == 0:
            tf_list[1] = False
            break
    return max(tf_list[0] * gcd_list[0], tf_list[1] * gcd_list[1] )

print(gcd(16,24))
print(gcd_all(16,24,32,50))
print(solution([10,17],[5,20]))
print(solution([10,20],[5,17]))
print(solution([14,35,119],[18,30,102]))