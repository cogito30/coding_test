# 피보나치 함수
T = int(input())
dp = [(1, 0), (0, 1)]

for i in range(2, 41):
    dp.append((dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]))

for _ in range(T):
    num = int(input())
    print(f"{dp[num][0]} {dp[num][1]}")
