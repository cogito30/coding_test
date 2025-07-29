# [한양대 HCPC 2023] Recovering the Region
import sys

N = int(input())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

for i in range(N):
    for _ in range(N):
        print(i + 1, end = " ")
    print()

""" bfs이지만 오답인 코드
import sys

N = int(input())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

visited = [[False for _ in range(N)] for _ in range(N)]
answer = [[0 for _ in range(N)] for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def bfs(start_row, start_col, check_list, count):
    q = []
    q.append((start_row, start_col))
    visited[start_row][start_col] = True
    answer[start_row][start_col] = count
    check_list.append(matrix[start_row][start_col])
    while len(q) > 0:
        r, c = q.pop(0)
        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]

            if new_r < 0 or new_r >= N or new_c < 0 or new_c >= N:
                continue
            if matrix[new_r][new_c] not in check_list:
                if not visited[new_r][new_c]:
                    q.append((new_r, new_c))
                    visited[new_r][new_c] = True
                    answer[new_r][new_c] = count
                    check_list.append(matrix[new_r][new_c])

count = 1
for row in range(N):
    for col in range(N):
        if not visited[row][col]:
            bfs(row, col, [], count)
            count += 1

for row in range(N):
    for col in range(N):
        print(answer[row][col], end=" ")
    print()
"""