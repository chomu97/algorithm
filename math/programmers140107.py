# 제 1사분면에 사분원을 그린다고 생각한다.
# x^2 + y^2 = d^2 인 원이 그려질 것이다.
# 0,0을 무조건 그린다고 생각 ( 가장 많이 그려질 것 )
# x=0 부터 x += k 를 하면서 위의 원의 방정식에서 빼면서 y값을 구한다.
# y=0 부터 y += k 를 하면서 sqrt(y)와 같거나 작을때까지 count를 더한다.

def solution(k, d):
    answer = 0
    for i in range(0, d+1, k):
        max_y = d*d - i*i
        answer += int(max_y ** 0.5)//k + 1
    return answer

print(solution(2,4))
print("----------")
print(solution(1,5))