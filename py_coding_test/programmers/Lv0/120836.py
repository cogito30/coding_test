# 순서쌍의 개수
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if i * i > n:
            break
        elif i * i == n:
            answer += 1
        elif n % i == 0:
            answer += 2
        
    return answer