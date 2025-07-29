# 금고털이
import sys

W, N = map(int, input().split())
metals = [0 for _ in range(10**4+1)]  # index = price, value = metal_count
for i in range(N):
    M, P = map(int, input().split())
    metals[P] += M


answer = 0
total_weight = 0
for i in range(len(metals)-1, 0, -1):
    if metals[i] != 0:
        total_weight += metals[i]
        answer += metals[i] * i
    if total_weight >= W:
        diff_weight = total_weight - W
        answer -= diff_weight * i
        break

print(answer)

""" 시간초과
W, N = map(int, input().split())
metals = [0 for i in range(N)]
for i in range(N):
    M, P = map(int, input().split())
    metals[i] = (P, M)

metals.sort(reverse=True)

answer = 0
total_weight = 0
for price, weight in metals:
    total_weight += weight 
    answer += weight * price
    if total_weight >= W:
        diff_weight = total_weight - W
        answer -= diff_weight * price
        break

print(answer)
"""