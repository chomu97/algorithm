def solution(phone_book):
    phone_book = sorted(phone_book, key=lambda x: (x, len(x)))
    for i, phone in enumerate(phone_book[:-1]):
        if phone_book[i+1].startswith(phone):
            return False
    return True

def solution_hash(phone_book):
    phone_dict = {}
    for phone in phone_book:
        phone_dict[phone] = 1
    for phone in phone_book:
        tmp = ""
        for i in phone:
            tmp += i
            if tmp in phone_dict and tmp != phone:
                return False
    return True

print(solution_hash(["119", "97674223", "1195524421"]))
print(solution_hash(["123","456","789"]))
print(solution_hash(["12","123","1235","567","88"]))