# ACM 호텔
T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    q, r = N % H, N//H + 1
    if q == 0:
        q = H
        r = N//H
    answer = q * 100 + r
    print(answer)