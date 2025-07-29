# 블랙잭
N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum_num = cards[i] + cards[j] + cards[k]
            if sum_num <= M and sum_num > max_sum:
                max_sum = sum_num
print(max_sum)