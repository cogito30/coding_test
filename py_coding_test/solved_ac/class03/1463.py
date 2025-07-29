# 1로 만들기
N = int(input())
dp = [0, 0, 1, 1]
for i in range(4, N+1):
    num = dp[i-1]
    if i % 3 == 0:
        num = min(num, dp[i//3])
    if i % 2 == 0:
        num = min(num, dp[i//2])
    dp.append(num + 1)
print(dp[N])