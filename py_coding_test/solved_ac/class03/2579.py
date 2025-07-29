# 계단 오르기
N = int(input())
scores = []
for _ in range(N):
    score = int(input())
    scores.append(score)

if N < 4:
    if N == 1:
        print(scores[0])
    elif N == 2:
        print(scores[0] + scores[1])
    elif N == 3:
        print(max(scores[0], scores[1]) + scores[2])
else:
    dp = [scores[0], scores[0] + scores[1], max(scores[0], scores[1]) + scores[2]]
    for i in range(3, N):
        max_score = max(dp[i-2], dp[i-3] + scores[i-1])
        dp.append(max_score + scores[i])
    print(dp[N-1])