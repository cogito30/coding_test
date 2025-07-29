# 웰컴 키트
N = int(input())
t_shirt = list(map(int, input().split()))
T, P = map(int, input().split())

count = 0
for i in range(6):
    q = t_shirt[i] // T + 1
    if t_shirt[i] % T == 0:
        q -= 1
    count += q

print(count)
print(N//P , N % P)