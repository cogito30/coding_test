# 정수를 나선형으로 배치하기
def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    row_start = 0
    row_end = n
    col_start = 0
    col_end = n
    i = 1
    while i <= n*n:
        for col in range(col_start, col_end):
            answer[row_start][col] = i
            i += 1
        row_start += 1
        for row in range(row_start, row_end):
            answer[row][col_end-1] = i
            i += 1
        col_end -= 1
        for col in range(col_end-1, col_start-1,-1):
            answer[row_end-1][col] = i
            i += 1
        row_end -= 1
        for row in range(row_end-1, row_start-1, -1):
            answer[row][col_start] = i
            i += 1
        col_start += 1
        
    return answer