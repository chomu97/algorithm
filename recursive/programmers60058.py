"""
def func_a(p):
    if w == "":
        return ""
    else:
        u, v = w 분리 로직 실행( 앞에서 각각의 개수를 세면서 가다가 같아지는 순간 리턴)
        if u가 올바른 괄호 문자열:
            return u + func_a(v)
        else:
            result = "(" + func_a(v) + ")"
            u = u[1:-1]
            result2 = ""
            for bracket in u:
                result2 += 괄호 뒤집기. ( 딕셔너리 이용할 예정 )
            return result + result2

def split_bracket(p):
    count = {'(': 0, ')': 0}
    for enumerate(p):
        count[v] += 1
        if count['('] == count[')']:
            break
    return "(" * count["("] + ")" * count[")"], p[i:]
"""


def split_bracket(p):
    count = {'(': 0, ')': 0}
    result1 = ""
    for i, v in enumerate(p):
        count[v] += 1
        result1 += v
        if count['('] == count[')']:
            result2 = p[i+1:]
            break
    return result1, result2


def is_right_bracket(p):
    stack = [p[0]]
    for br in p[1:]:
        if br == "(":
            stack.append(br)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


def change_bracket(w):
    change = {"(": ")", ")":"("}
    if w == "":
        return ""
    else:
        u, v = split_bracket(w)
        if is_right_bracket(u):
            return u + change_bracket(v)
        else:
            result1 = "(" + change_bracket(v) + ")"
            u = u[1:-1]
            result2 = ""
            for br in u:
                result2 += change[br]
            return result1 + result2


def solution(p):
    # a, b = split_bracket(p)
    # print("a : " + a)
    # print("b : " + b)
    # print("===============")
    # print(change_bracket(p))
    return change_bracket(p)


solution("(()())()")
solution("()))((()")
solution(")(")
# solution(")))(((")