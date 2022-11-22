def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp1 = get_binary_num(arr1[i], [])
        tmp2 = get_binary_num(arr2[i], [])
        while len(tmp1) < n:
            tmp1.append(0)
        while len(tmp2) < n:
            tmp2.append(0)
        tmp1.reverse()
        tmp2.reverse()
        decrypted = ['#' if a or b else ' ' for a,b in zip(tmp1,tmp2)]
        answer.append(''.join(decrypted))
    return answer


def get_binary_num(n, lst):
    a, b = divmod(n, 2)
    lst.append(b)
    if a == 0:
        return lst
    else:
        return get_binary_num(a, lst)

print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))

# ans = get_binary_num(9, [])
# ans.reverse()
# print(ans)