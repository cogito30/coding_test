# 나무 공격
import sys

n, m = map(int, input().split())

board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

for _ in range(2):
    r1, r2 = map(int, input().split())
    for row in range(r1-1, r2):
        for col in range(m):
            if board[row][col] == 1:
                board[row][col] = 0
                break

answer = 0
for row in range(n):
    for col in range(m):
        if board[row][col] == 1:
            answer += 1
            
print(answer)