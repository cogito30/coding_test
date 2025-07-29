# GBC
import sys

N, M = map(int, input().split())

limit = []
total_length = 0
for _ in range(N):
    length, velocity = map(int, input().split())
    total_length += length
    limit.append((total_length, velocity))

max_velocity = 0
total_length = 0
i = 0
for _ in range(M):
    length, velocity = map(int, input().split())
    total_length += length
    while True:
        if total_length == limit[i][0]:
            max_velocity = max(velocity - limit[i][1], max_velocity)
            i += 1
            break
        elif total_length > limit[i][0]:
            max_velocity = max(velocity - limit[i][1], max_velocity)
            i += 1
        elif total_length <= limit[i][0]:
            max_velocity = max(velocity - limit[i][1], max_velocity)
            break
print(max_velocity)
            