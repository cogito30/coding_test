# 전국 대회 선발 고사
def solution(rank, attendance):
    answer = 0
    attendance_rank = []
    for i, r in enumerate(rank):
        if attendance[i]:
            attendance_rank.append((r, i))
    attendance_rank.sort()
    for i in range(3):
        answer *= 100
        answer += attendance_rank[i][1]
        
    return answer