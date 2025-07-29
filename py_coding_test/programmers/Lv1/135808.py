# 과일 장수
def solution(k, m, score):
    answer = 0
    score.sort()
    total_len = (len(score) // m) * m
    for i in range(len(score) - total_len, len(score), m):
        answer += score[i] * m
    return answer