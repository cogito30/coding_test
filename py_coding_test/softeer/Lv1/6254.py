# 근무 시간
import sys

total = 0
for i in range(5):
    start, end = input().split()
    total += (int(end[0:2]) - int(start[0:2])) * 60
    total += int(end[3:5]) - int(start[3:5])

print(total)
