# 안전지대
def solution(board):
    answer = 0
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    M, N = len(board), len(board[0])
    boardCopy = [[board[i][j] for j in range(N)] for i in range(M)]
    def checkBomb(x, y):
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (nx < 0 or ny < 0 or nx >= M or ny >= N):
                continue
            boardCopy[nx][ny] = 1
            
    for i in range(M):
        for j in range(N):
            if board[i][j] == 1:
                checkBomb(i, j)
    
    for i in range(M):
        for j in range(N):
            if boardCopy[i][j] == 0:
                answer += 1

    return answer