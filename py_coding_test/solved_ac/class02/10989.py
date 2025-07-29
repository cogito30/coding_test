# 수 정렬하기 3
# 일반 정렬 메서드 사용시 메모리 초과 
import sys

input = sys.stdin.readline
N = int(input())
num_list = [0 for _ in range(10_001)]

for _ in range(N):
    num = int(input())
    num_list[num] += 1

for idx, num in enumerate(num_list):
    for _ in range(num):
        print(idx)