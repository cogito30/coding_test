# 최댓값 만들기 (1)
def solution(numbers):
    answer = 0
    numbers.sort()
    answer = numbers[-1] * numbers[-2]
    return answer