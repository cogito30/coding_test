# 파도반 수열
T = int(input())
dp = [0, 1, 1, 1, 2, 2]
for i in range(6, 101):
    dp.append(dp[i-1] + dp[i-5])

for _ in range(T):
    N = int(input())
    print(dp[N])