# 최댓값 만들기 (2)
def solution(numbers):
    answer = 0
    numbers.sort()
    a = numbers[0] * numbers[1]
    b = numbers[-2] * numbers[-1]
    answer = max(a, b)
    return answer