from collections import deque

N, M, R = map(int, input().split())
arr = []
answer = [[0] * M for _ in range(N)]
for _ in range(N):
    arr.append(list(map(int,input().split())))

start_row = -1
start_col = 0
while M > 0 and N > 0:
    temp = deque()
    row = start_row
    col = start_col
    for _ in range(N):
        row += 1
        temp.append(arr[row][col])
    for _ in range(M-1):
        col += 1
        temp.append(arr[row][col])
    for _ in range(N-1):
        row -= 1
        temp.append(arr[row][col])
    for _ in range(M-2):
        col -= 1
        temp.append(arr[row][col])
    temp.rotate(R)
    row = start_row
    col = start_col
    for _ in range(N):
        row += 1
        answer[row][col] = temp.popleft()
    for _ in range(M - 1):
        col += 1
        answer[row][col] = temp.popleft()
    for _ in range(N - 1):
        row -= 1
        answer[row][col] = temp.popleft()
    for _ in range(M - 2):
        col -= 1
        answer[row][col] = temp.popleft()

    start_row += 1
    start_col += 1
    M -= 2
    N -= 2
for a in answer:
    print(' '.join(map(str,a)))



# 주니온TV 풀이
def get_chain(k, n, m, A):
    C = [0] * ((n + m - 2) * 2)
    i, j, t = k, k, 0
    for _ in range(n - 1):
        C[t] = A[i][j]
        i += 1; t += 1
    for _ in range(m - 1):
        C[t] = A[i][j]
        j += 1; t += 1
    for _ in range(n - 1):
        C[t] = A[i][j]
        i -= 1; t += 1
    for _ in range(m - 1):
        C[t] = A[i][j]
        j -= 1; t += 1
    return C


def put_chain(C, k, n, m, A):
    i, j, t = k, k, 0
    for _ in range(n - 1):
        A[i][j] = C[t]
        i += 1;
        t += 1
    for _ in range(m - 1):
        A[i][j] = C[t]
        j += 1;
        t += 1
    for _ in range(n - 1):
        A[i][j] = C[t]
        i -= 1;
        t += 1
    for _ in range(m - 1):
        A[i][j] = C[t]
        j -= 1;
        t += 1
    return C

def rotate(k, n, m, r, A):
    chain = get_chain(k, n, m, A)
    pos = len(chain) - (r % len(chain))
    rotated = chain[pos:] + chain[:pos]
    put_chain(rotated, k, n, m, A)


def solve(n, m, r, A):
    for k in range(min(n, m) // 2):
        rotate(k, n - 2*k, m - 2*k, r, A)
    for i in range(n):
        print(" ".join(map(str, A[i])))

n, m, r = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
solve(n, m, r, A)