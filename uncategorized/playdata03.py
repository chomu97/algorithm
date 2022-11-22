sub = int(input())
scores = list()
answer = list()
for i in range(sub):
    scores.append(list(map(int, input().split())))

for score in scores:
    if score[0] * score[2]/100 > score[1]:
        tmp = [1 if i > score[4] else 0 for i in score[5:]]
        answer.append(sum(tmp) == score[3])
    else:
        answer.append(False)

print(int(sum(answer) == sub))