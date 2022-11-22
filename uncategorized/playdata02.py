size = int(input())
skin = list()
for i in range(size):
    skin.append(list(map(int, input().split())))


max_width_idx, min_width_idx = 0, size
max_height_idx, min_height_idx = 0, size
for row in range(size):
    for col in range(size):
        if skin[row][col]:
            if max_width_idx < col:
                max_width_idx = col
            if max_height_idx < row:
                max_height_idx = row
            if min_width_idx > col:
                min_width_idx = col
            if min_height_idx > row:
                min_height_idx = row

print((max_height_idx - min_height_idx + 1) * (max_width_idx - min_width_idx + 1))