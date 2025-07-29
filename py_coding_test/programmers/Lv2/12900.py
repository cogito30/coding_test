# 2 x n 타일링
def solution(n):
    answer = 0
    dp = [1, 2]
    for i in range(n):
        dp.append((dp[i]+dp[i+1]) % 1_000_000_007)
    answer = dp[n-1]
    return answer