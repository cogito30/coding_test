# 삼각형의 완성조건 (2)
def solution(sides):
    answer = 0
    max_len = max(sides)
    min_len = min(sides)
    for i in range(1, max_len):
        if max_len < (min_len + i) and i <= max_len:
            answer += 1
    for i in range(1, sum(sides)):
        if i < sum(sides) and i >= max_len:
            answer += 1
            
    return answer