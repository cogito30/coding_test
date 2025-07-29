# 택배 상자 꺼내기
def solution(n, w, num):
    answer = 0
    row_len = (n-1) // w + 1
    col_len = w
    board = [[0 for _ in range(col_len)] for _ in range(row_len)]
    num_row = 0
    for i in range(1, n+1):
        row = (i - 1) // w
        col = (i - 1) % w
        if num == i:
            num_row = row
        if row % 2 == 1:
            board[row][w - col - 1] = i
        else:
            board[row][col] = i

    num_col = board[num_row].index(num)
    
    for row in range(num_row, row_len):
        if board[row][num_col] != 0:
            answer += 1
    
    return answer 