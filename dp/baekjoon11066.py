"""
N = int(input())
for _ in range(N):
    M = int(input())
    files = list(map(int, input().split()))
    dp = [[0] * M for _ in range(M)]
    files_sum = [[0] * M for _ in range(M)]
    for col in range(M):
        for row in range(col, -1, -1):
            if row == col:
                files_sum[row][col] = files[col]
            if row != col:
                files_sum[row][col] = files_sum[row][col-1]+files_sum[col][col]
                # print([dp[row][i-1]+dp[i][col] fo])
    for i in range(M):
        print(files_sum[i])
    for col in range(M):
        for row in range(col, -1, -1):
            # if row == col:
            #     dp[row][col] = files[col]
            if row != col:
                temp = []
                # if col < 4:
                for i in range(col,row,-1):
                    if row == i-1 and col == i:
                        temp.append(files[i-1] + files[i])
                    # elif row == i-1:
                    #     temp.append(dp[row][i-1] + dp[i][col] * 2)
                    # elif col == i:
                    #     temp.append(dp[row][i-1] * 2 + dp[i][col])
                    else:
                        temp.append(dp[row][i-1] + dp[i][col] + files_sum[row][col])
                print(temp)
                dp[row][col] = min(temp)
                # else:
                # for i in range(col, row, -1):
                #     if i == col:
                #         if dp[row][i]:
                #             temp.append(dp[row][i])
                #             print(f"row={row}, col={col}, dp={dp[row][i]}")
                #     elif i == row+1:
                #         if dp[i][col]:
                #             temp.append(dp[i][col])
                #             print(f"row={row}, col={col}, dp={dp[i][col]}")
                #     else:
                #         if dp[row][i] and dp[col+1-i][col]:
                #             temp.append(dp[row][i]+dp[col+1-i][col])
                #             print(f"row={row}, col={col}, dp1={dp[row][i]}, dp2={dp[col+1-i][col]}")
                # if temp:
                #     dp[row][col] = min(temp) + files_sum[row][col]
                # else:
                #     dp[row][col] = files_sum[row][col]



    for i in range(M):
        print(dp[i])
    # for col in range(M):
    #     for row in range(col, 0, -1):
    #         print(col, row)

# 위의 코드를 정리하면 다음과 같음.
"""
N = int(input())
for _ in range(N):
    M = int(input())
    files = list(map(int, input().split()))
    dp = [[0] * M for _ in range(M)]
    files_sum = [[0] * M for _ in range(M)]
    for col in range(M):
        for row in range(col, -1, -1):
            if row == col:
                files_sum[row][col] = files[col]
            if row != col:
                files_sum[row][col] = files_sum[row][col-1]+files_sum[col][col]
    for col in range(M):
        for row in range(col, -1, -1):
            if row != col:
                temp = []
                for i in range(col,row,-1):
                    if row == i-1 and col == i:
                        temp.append(files[i-1] + files[i])
                    else:
                        temp.append(dp[row][i-1] + dp[i][col] + files_sum[row][col])
                dp[row][col] = min(temp)
    print(dp[0][-1])