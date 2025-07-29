# 행렬 덧셈
N, M = map(int, input().split())

matrix1 = []
for i in range(N):
    matrix1.append(list(map(int, input().split())))

matrix2 = []
for i in range(N):
    matrix2.append(list(map(int, input().split())))

matrix = [[0 for _ in range(M)] for _ in range(N)]
for row in range(N):
    for col in range(M):
        matrix[row][col] = matrix1[row][col] + matrix2[row][col]

for row in range(N):
    for col in range(M):
        print(matrix[row][col], end=" ")
    print()