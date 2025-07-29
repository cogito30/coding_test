# 겹치는 선분의 길이
def solution(lines):
    answer = 0
    check_line = [0 for _ in range(-100, 101)]
    for line in lines:
        for i in range(line[0], line[1]):
            check_line[100+i] += 1
    for i in check_line:
        if i >= 2:
            answer += 1

    return answer