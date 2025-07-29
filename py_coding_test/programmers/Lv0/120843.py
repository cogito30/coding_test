# 공 던지기
def solution(numbers, k):
    answer = numbers[2*(k-1) % len(numbers)]
    return answer
"""
def solution(numbers, k):
    # [1, 2, 3], 5 / 3
    answer = (2*k-1) % len(numbers)
    if answer == 0:
        answer = len(numbers)
    
    return answer
"""