# 세 개의 구분자
def solution(myStr):
    answer = []
    newStr = myStr.replace("a", " ").replace("b", " ").replace("c", " ")
    for i in newStr.split(" "):
        if i != "":
            answer.append(i)
    if len(answer) == 0:
        answer.append("EMPTY")
    return answer