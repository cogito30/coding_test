# 나무 심기
import sys

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

a = arr[0] * arr[1]
b= arr[len(arr) - 2] * arr[len(arr) - 1]
max_val = a if a > b else b
print(max_val)