# 숨어있는 숫자의 덧셈 (1)
def solution(my_string):
    answer = 0
    for i in my_string:
        if i in "1234567890":
            answer += int(i)
    return answer