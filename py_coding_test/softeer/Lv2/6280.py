# 지도 자동 구축
import sys

N = int(input())

answer = 0
dot = 2
for i in range(N):
    dot += (dot - 1)
answer = dot ** 2
print(answer)