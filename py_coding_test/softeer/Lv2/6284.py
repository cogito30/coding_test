# 바이러스
import sys

K, P, N = map(int, input().split())

for _ in range(N):
    K = (K * P) % 1000000007

print(K)