# 팩토리얼
def solution(n):
    answer = 1
    # n = 1, n = 2일 경우 주의     
    if n == 1:
        return answer
    for i in range(1, n + 1):
        answer *= i
        if answer == n:   
            answer = i
            break
        elif answer > n:
            answer = i - 1
            break
    return answer