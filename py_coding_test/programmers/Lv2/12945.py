# 피보나치 수
def solution(n):
    answer = 0
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % 1234567
    answer = a
    return answer