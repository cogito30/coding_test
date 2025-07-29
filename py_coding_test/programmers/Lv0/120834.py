# 외계행성의 나이
def solution(age):
    answer = ''
    for i in str(age):
        answer += chr(int(i) + ord("a"))
    return answer