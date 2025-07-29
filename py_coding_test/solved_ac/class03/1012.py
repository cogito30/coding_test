# 유기농 배추
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0 for _ in range(M)]for _ in range(N)]
    visited = [[False for _ in range(M)]for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1

    def bfs(start_row, start_col, board, visited):
        q = []
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        q.append((start_row, start_col))
        visited[start_row][start_col] = True
        count = 1
        while q:
            cur_row, cur_col = q.pop(0)
            for i in range(4):
                nr = cur_row + dr[i]
                nc = cur_col + dc[i]
                if nr < 0 or nr >= N or nc < 0 or nc >= M:
                    continue
                if not visited[nr][nc] and board[nr][nc] == 1:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    count += 1
        return count

    answer = 0
    for r in range(N):
        for c in range(M):
            if not visited[r][c] and board[r][c] == 1 and bfs(r, c, board, visited) > 0:
                answer += 1
    print(answer)
    