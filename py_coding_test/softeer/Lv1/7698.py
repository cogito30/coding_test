# [한양대 HCPC 2023] 개표
import sys

n = int(input())

arr = list()
for i in range(n):
    arr.append(int(input()))

for i in range(n):
    q = arr[i] // 5;
    r = arr[i] % 5;
    for j in range(q):
        print("++++ ", sep="", end="")
    for k in range(r):
        print("|", sep="", end="")

    print()
