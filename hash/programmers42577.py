def solution(phone_book):
    phone_book = sorted(phone_book, key=lambda x: (x, len(x)))
    for i, phone in enumerate(phone_book[:-1]):
        if phone_book[i+1].startswith(phone):
            return False
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))