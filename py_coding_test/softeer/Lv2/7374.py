# 진정한 효도
import sys

board = []
for _ in range(3):
    row = list(map(int, input().split()))
    board.append(row)

answer = 3
for row in range(3):
    row_set = set(board[row])
    if len(row_set) == 1:
        answer = 0
        break
    elif len(row_set) == 2 and answer >= 2:
        answer = max(row_set) - min(row_set)
    elif len(row_set) == 3 and answer >= 3:
        answer = 2

for col in range(3):
    col_list = [board[0][col], board[1][col], board[2][col]]
    col_set = set(col_list)
    if len(col_set) == 1:
        answer = 0
        break
    elif len(col_set) == 2 and answer >= 2:
        answer = max(col_set) - min(col_set)
    elif len(col_set) == 3 and answer >= 3:
        answer = 2

print(answer)