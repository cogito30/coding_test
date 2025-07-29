# 게임 맵 최단거리
def solution(maps):
    #반례: [[1], [1]] / 2
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False for _ in range(m+1)] for _ in range(n+1)]
    board = [[1 for _ in range(m+1)] for _ in range(n+1)]
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    def bfs(r, c): 
        queue = []
        queue.append((r, c))
        visited[r][c] = True # BFS 주의
        while queue:
            r, c = queue.pop(0)
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < 1 or nc < 1 or nr > n or nc > m:
                    continue
                if not visited[nr][nc] and maps[nr-1][nc-1] == 1:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    board[nr][nc] = board[r][c] + 1
        if not visited[n][m]:
            return -1
        return board[n][m]
    
    answer = bfs(1, 1)
                
    return answer