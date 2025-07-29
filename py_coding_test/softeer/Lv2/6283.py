# 8단 변속기
import sys

data = list(map(int, input().split()))

state = 1
if data[0] < data[1]:
    state = 1
elif data[0] > data[1]:
    state = 2

for i in range(7):
    if data[i] < data[i+1] and state == 1:
        state = 1
    elif data[i] > data[i+1] and state == 2:
        state = 2
    else:
        state = 3

answer = ""
if state == 1:
    answer = "ascending"
elif state == 2:
    answer = "descending"
else:
    answer = "mixed"
print(answer)