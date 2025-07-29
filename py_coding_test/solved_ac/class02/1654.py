# 랜선 자르기
## 이진 탐색
K, N = map(int, input().split())
cable = []
for _ in range(K):
    length = int(input())
    cable.append(length)

start = 1
end = max(cable)
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in cable:
        count += i // mid
    if count >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)


"""시간초과
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
cable = []
for _ in range(K):
    length = int(input())
    cable.append(length)

max_cable = max(cable)
answer = 0
while True:
    count = 0
    for i in range(K):
        count += cable[i] // max_cable

    if count >= N:
        answer = max_cable
        break
    else:
        max_cable -= 1

print(answer)

"""