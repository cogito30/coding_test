# 두 정수 사이의 합
def solution(a, b):
    answer = 0
    low_val = min(a, b)
    high_val = max(a, b)
    for i in range(low_val, high_val + 1):
        answer += i
    return answer