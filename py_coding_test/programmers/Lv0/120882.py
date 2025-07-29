# 등수 매기기
def solution(score):
    answer = []
    avg_score = []
    for s in score:
        avg_score.append(sum(s)/2)
    sorted_avg_score = sorted(avg_score, reverse=True)
    
    for i in avg_score:
        answer.append(sorted_avg_score.index(i)+1)
    return answer