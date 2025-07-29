# [한양대 HCPC 2023] X marks the Spot
import sys

N = int(input())
answer = []
for _ in range(N):
    A, B = input().split()
    for i in range(len(A)):
        if A[i] == "X" or A[i] == "x":
            answer.append(B[i].upper())
            break
answer = ''.join(answer)
print(answer)

""" 시간초과
N = int(input())
answer = ""
for _ in range(N):
    A, B = input().split()
    index = 0
    for i in range(len(A)):
        if A[i] == "X" or A[i] == "x":
            index = i
            break
    answer += B[index]
    
print(answer.upper())
"""