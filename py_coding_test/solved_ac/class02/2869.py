# 달팽이는 올라가고 싶다
A, B, V = map(int, input().split())
# V == A + (A-B) * (i-1)
answer = (V - A) // (A- B) + 1
if (V - A) % (A - B) != 0:
    answer += 1
print(answer)

""" 시간초과
A, B, V = map(int, input().split())

answer = 0
total_dist = 0
while True:
    answer += 1
    total_dist += A
    if total_dist >= V:
        break
    else:
        total_dist -= B
print(answer)
"""