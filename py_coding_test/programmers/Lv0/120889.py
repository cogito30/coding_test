# 삼각형의 완성조건 (1)
def solution(sides):
    answer = 0
    maxVal = max(sides)
    totalSum = sum(sides)
    if maxVal < (totalSum - maxVal):
        answer = 1
    else:
        answer = 2
    return answer