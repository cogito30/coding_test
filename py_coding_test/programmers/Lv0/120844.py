# 배열 회전시키기
def solution(numbers, direction):
    answer = []
    if direction == "right":
        answer = numbers[-1:] + numbers[:-1]
    else:
        answer = numbers[1:] + numbers[:1]
    return answer