# 2xn 타일링 2
n = int(input())
dp = [1, 3]
for i in range(n):
    dp.append((dp[i]*2 + dp[i+1]) % 10_007) 
print(dp[n-1])