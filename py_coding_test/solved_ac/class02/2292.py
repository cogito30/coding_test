# 벌집
N = int(input())

answer = 1
total_num = 1
while total_num < N:
    if N > answer and N <= answer:
        break
    total_num += 6 * (answer)
    answer += 1
print(answer)