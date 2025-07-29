# 구슬을 나누는 경우의 수
def solution(balls, share):
    answer = 0
    a, b = 1, 1
    for i in range(share + 1, balls + 1):
        a *= i
    for j in range(1, balls - share + 1):
        b *= j
    answer = a//b
    return answer