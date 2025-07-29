# 성적 평균
import sys

N, K = map(int, input().split())
S = list(map(int, input().split()))
for _ in range(K):
    start, end = map(int, input().split())
    print(sum(S[start-1:end])/(end-start+1))