# 모음 제거
def solution(my_string):
    answer = ''
    data = ['a', 'e', 'i', 'o', 'u']
    for i in my_string:
        if i not in data:
            answer += i
    return answer