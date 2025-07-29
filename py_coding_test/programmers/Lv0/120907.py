# OX퀴즈
def solution(quiz):
    answer = []
    for q in quiz:
        a, b = q.split("=")
        if eval(a) == int(b):
            answer.append("O")
        else:
            answer.append("X")
    return answer