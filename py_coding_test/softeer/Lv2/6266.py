# [21년 재직자 대회 예선] 회의실 예약
import sys

N, M = map(int, input().split())

room_name = []
for i in range(N):
    name = input()
    room_name.append(name)

room_name.sort()
room_time = {}
for name in room_name:
    room_time[name] = [0 for _ in range(9, 18)]

for _ in range(M):
    r, s, t = input().split()
    s, t = int(s), int(t)
    for time in range(s-9, t-9):
        room_time[r][time] = 1


for idx, key in enumerate(room_time.keys()):
    print(f"Room {key}:")
    count = 0
    answer = []
    interval = ""
    for time in range(9, 18):
        if room_time[key][time-9] == 0 and time == 9:
            interval += "09"
        if room_time[key][time-9] == 0 and time == 17:
            interval += "-18"
            answer.append(interval)
            count += 1
            interval = ""
        elif time == 17:
            break
        elif room_time[key][time-9] == 0 and room_time[key][time-8] == 1:
            interval += f"-{str(time+1)}"
            answer.append(interval)
            count += 1
            interval = ""
        elif room_time[key][time-9] == 1 and room_time[key][time-8] == 0:
            interval += f"{str(time+1)}"

    if count == 0:
        print(" Not available")
    else:
        print(f"{count} available:")
    for time in answer:
        print(time)
    if idx != N - 1:
        print("-----")
