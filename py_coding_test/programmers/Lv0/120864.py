# 숨어있는 숫자의 덧셈 (2)
def solution(my_string):
    answer = 0
    tmpStr = ""
    for i in range(len(my_string)):
        if my_string[i].isdigit():
            tmpStr += my_string[i]
        elif len(tmpStr) > 0:
            answer += int(tmpStr)
            tmpStr = ""
        if i == len(my_string) - 1 and len(tmpStr) > 0:
            answer += int(tmpStr)
            
    return answer