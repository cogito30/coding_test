# 구간 합 구하기 4
## input() 사용시 시간초과 sys.stdin.readline 사용
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))

sum_of_num = 0
interval_sum = [0]
for i in range(N):
    sum_of_num += num_list[i]
    interval_sum.append(sum_of_num)

for _ in range(M):
    a, b = map(int, input().split())
    print(interval_sum[b]-interval_sum[a-1])