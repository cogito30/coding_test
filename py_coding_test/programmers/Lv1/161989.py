# 덧칠하기
def solution(n, m, section):
    answer = 0
    roller_idx = 0 # 시작 위치
    for i in section:
        if i >= roller_idx:
            answer += 1
            roller_idx = i + m
            
    return answer