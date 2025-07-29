# A + B
import sys

n = int(input())

for i in range(n):
    a, b = input().split()
    a, b = int(a), int(b)
    print(f"Case #{i + 1}: {a + b}")
