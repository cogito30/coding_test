# 정수 제곱근 판별
def solution(n):
    answer = -1
    for i in range(1, n + 1):
        if i * i == n:
            answer = (i + 1) ** 2
            break
        
    return answer