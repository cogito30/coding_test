# 글자 지우기
def solution(my_string, indices):
    answer = ''
    strList = [i for i in my_string]
    for idx, ch in enumerate(strList):
        if idx not in indices:
            answer += ch
    return answer