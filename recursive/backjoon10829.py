def dec2bin(num):
    if num == 1 or num == 0:
        return str(num)
    else:
        return dec2bin(num // 2) + str(num % 2)

n = int(input())
print(dec2bin(n))
print(bin(n)[2:]) # 2진수로 변환해주는 bin을 이용하여 0b를 자르고 출력 가능.