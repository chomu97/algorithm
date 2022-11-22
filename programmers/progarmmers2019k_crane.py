from collections import defaultdict
def solution(board, moves):
    answer = 0
    stack = []
    board_dict = defaultdict(list)
    for i in range(len(board)):
        for data in board[::-1]:
            if data[i] != 0:
                board_dict[i].append(data[i])
    for move in moves:
        if board_dict[move-1]:
            p = board_dict[move-1].pop()
            if not stack or stack[-1] != p:
                stack.append(p)
            else:
                stack.pop()
                answer += 2
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
solution(board,moves)