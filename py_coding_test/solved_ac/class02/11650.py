# 좌표 정렬하기
N = int(input())

coordinate = []
for _ in range(N):
    x, y = map(int, input().split())
    coordinate.append((x, y))
coordinate.sort()

for x,y in coordinate:
    print(f"{x} {y}")
