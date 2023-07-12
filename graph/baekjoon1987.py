# def dfs(board, R, C):
#     stack = [(board[0][0], 0, 0)]
#     visited = [[0 for _ in range(C)] for _ in range(R)]
#     visited[0][0] = 1
#
#     d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
#     result = 0
#     result_string = ''
#     while stack:
#         string, row, col = stack.pop()
#         # if len(string) < visited[row][col]:
#         #     continue
#         # else:
#         visited[row][col] = len(string)
#         if result <= len(string):
#             result = len(string)
#             result_string = string
#         # print(row, col, stack, result_string, sep='\t')
#         for dy, dx in d:
#             dr, dc = row + dy, col + dx
#             if 0 <= dr < R and 0 <= dc < C:
#                 if board[dr][dc] not in string:
#                     stack.append((string+board[dr][dc], dr, dc))
#                     # visited[dr][dc] = True
#
#     return result, result_string





R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

# print(board)
# print(dfs(board, R, C))
answer = 0
visited = [False for _ in range(26)]
visited[ord(board[0][0]) - ord('A')] = True

def dfs2(row, col, visited, cnt):
    global answer
    answer = max(answer, cnt)

    d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dy, dx in d:
        dr, dc = row + dy, col + dx
        if 0 <= dr < R and 0 <= dc < C:
            curr = ord(board[dr][dc]) - ord('A')
            if not visited[curr]:
                visited[curr] = True
                dfs2(dr, dc, visited, cnt + 1)
                visited[curr] = False


dfs2(0, 0, visited, 1)
print(answer)