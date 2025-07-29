# 주행거리 비교하기
import sys

a, b = input().split()
a, b = int(a), int(b)

if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("same")