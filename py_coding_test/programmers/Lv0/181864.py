# 문자열 바꾸서 찾기
def solution(myString, pat):
    answer = 0
    changeString = ""
    for i in myString:
        if i == "A":
            changeString += "B"
        else:
            changeString += "A"
    if pat in changeString:
        answer = 1
    else:
        answer = 0
    return answer