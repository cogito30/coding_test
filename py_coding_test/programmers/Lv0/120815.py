# 피자 나눠 먹기 (2)
def solution(n):
    answer = 0
    x = 0
    while True:
        x += 1
        if 6*x % n == 0:
            answer = x
            break
    return answer