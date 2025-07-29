# 문자열 정렬하기 (2)
def solution(my_string):
    answer = ''
    strList = []
    for i in my_string.lower():
        strList.append(i)
    strList.sort()
    answer = ''.join(strList)
    return answer