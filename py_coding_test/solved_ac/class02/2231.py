# 분해합
N = int(input())

answer = 0
result = 0
for i in range(1, N + 1):
    result = i + sum(list(map(int, str(i))))
    if result == N:
        answer = i
        break
    if i == N:
        answer = 0
        break
print(answer)
    