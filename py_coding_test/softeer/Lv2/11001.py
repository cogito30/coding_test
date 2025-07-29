# GPT식 숫자 비교
import sys

N = int(input())
data = []
for _ in range(N):
    a = list(map(int, input().split(".")))
    data.append(a)

data.sort()
for i in data:
    if len(i) > 1:
        print(str(i[0])+"."+str(i[1]))
    else:
        print(str(i[0]))