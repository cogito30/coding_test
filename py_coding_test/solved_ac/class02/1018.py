# 체스판 다시 칠하기
def check_board_color(start_row, start_col, board):
    white_start_count = 0
    black_start_count = 0
    for row in range(start_row, start_row + 8):
        for col in range(start_col, start_col + 8):
            if (row + col) % 2 == 0:
                if board[row][col] == "B":
                    white_start_count += 1
                elif board[row][col] == "W":
                    black_start_count += 1
            else:
                if board[row][col] == "W":
                    white_start_count += 1
                elif board[row][col] == "B":
                    black_start_count += 1
    return min(white_start_count, black_start_count)

N, M = map(int, input().split())
board = [[i for i in input()] for _ in range(N)]

result = []
for row in range(N - 7):
    for col in range(M - 7):
        result.append(check_board_color(row, col, board))
print(min(result))