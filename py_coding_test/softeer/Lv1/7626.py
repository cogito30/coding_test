# 연탄 배달의 시작
import sys

n = int(input())
arr = list(map(int, input().split()))

min_diff = 1000000
cnt = 0
for i in range(1, len(arr)):
    if (arr[i] - arr[i-1] < min_diff):
        min_diff = arr[i] - arr[i-1]
        cnt = 1
    elif (arr[i] - arr[i-1] == min_diff):
        cnt += 1

print(cnt)