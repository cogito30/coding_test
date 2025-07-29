# 문자열 나누기
def solution(s):
    answer = 0
    x_count = 0
    not_x = 0
    std_x = s[0]
    for i in range(len(s)):
        if std_x == "":
            std_x = s[i]
            
        if s[i] == std_x:
            x_count += 1
        else:
            not_x += 1
            
        if x_count == not_x:
            x_count = 0
            not_x = 0
            std_x = ""
            answer += 1
        elif i == len(s) - 1:
            answer += 1
            
    return answer