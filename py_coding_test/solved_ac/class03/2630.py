# 색종이 만들기
## 재귀 작성시 범위 주의!!
"""
with open('./solved_ac/class03/test.txt', 'r') as f:
    N = int(f.readline().strip())
    board = []
    for _ in range(8):
        cols = list(map(int, f.readline().split()))
        board.append(cols)
"""
N = int(input())
board = []
for _ in range(N):
    cols = list(map(int, input().split()))
    board.append(cols)

result = [0, 0]

def check_color(r, c, size):
    color = board[r][c]
    for row in range(r, r + size):
        for col in range(c, c + size):
            if color != board[row][col]:
                resize = size//2
                check_color(r, c, resize)
                check_color(r + resize, c, resize)
                check_color(r, c + resize, resize)
                check_color(r + resize, c + resize, resize)
                return
    result[color] += 1

check_color(0, 0, N)
for i in result:
    print(i)