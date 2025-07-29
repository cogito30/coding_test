# 2xn 타일링
n = int(input())

dp = [1, 2]
for i in range(n):
    dp.append((dp[i]+ dp[i+1]) % 10_007)

print(dp[n-1])