# 문자열 잘라서 정렬하기
def solution(myString):
    answer = []
    my_string = myString.split("x")
    for i in my_string:
        if i == "x" or i == "":
            continue
        else:
            answer.append(i)
    answer.sort()
    return answer