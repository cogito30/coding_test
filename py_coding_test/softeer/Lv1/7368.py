# 위험한 효도
import sys

a, b, d = map(int, input().split())

time = 0
move = 0
while (d > move):
    time += a
    move += a
    if (move >= d): 
        time -= (move - d)
        move = d
        break
    
    time += b;

    
while (2*d > move) and (move >= d):
    time += b
    move += b
    if (move >= 2*d):
        time -= (move - 2*d)
        move = 2*d
        break
    
    time += a


print(time)
