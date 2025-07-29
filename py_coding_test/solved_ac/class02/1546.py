# 평균
N = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)

total_score = 0
for score in scores:
    total_score += score*100/max_score

print(total_score/N)