# 연탄의 크기
import sys

n = int(input())

home_radius = list(map(int, input().split()))
max_radius = max(home_radius)

max_count = 0
for i in range(2, max_radius + 1):
    count = 0
    for radius in home_radius:
        if radius % i == 0:
            count += 1
    if count > max_count:
        max_count = count

print(max_count)