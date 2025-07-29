# 좌표 정렬하기 2
N = int(input())
coordinate = []
for _ in range(N):
    x, y = map(int, input().split())
    coordinate.append((x, y))
coordinate.sort(key=lambda x: (x[1], x[0]))

for x, y in coordinate:
    print(f"{x} {y}")