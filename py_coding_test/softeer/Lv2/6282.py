# 장애물 인식 프로그램
import sys
from collections import deque

N = int(input())

matrix = []
visited = []
for _ in range(N):
    rows = [int(i) for i in input()]
    matrix.append(rows)
    visited.append([0 for _ in range(N)])

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
q = deque()
def bfs(start_row, start_col):
    q.append((start_row, start_col))
    visited[start_row][start_col] = 1
    count = 1
    
    while len(q) > 0:
        r, c = q.popleft()
        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]
            if new_r < 0 or new_c < 0 or new_r >= N or new_c >= N:
                continue
            if matrix[new_r][new_c] == 1 and visited[new_r][new_c] == 0:
                visited[new_r][new_c] = 1
                count += 1
                q.append((new_r, new_c))
    return count

answer = []
total_block = 0
for row in range(N):
    for col in range(N):
        if visited[row][col] == 0 and matrix[row][col] == 1:
            cnt = bfs(row, col)
            if cnt != 0:
                answer.append(cnt)
                total_block += 1
answer.sort()
print(total_block)
for i in answer:
    print(i)
    