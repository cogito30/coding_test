# 부분 문자열 이어 붙여 문자열 만들기
def solution(my_strings, parts):
    answer = ""
    for idx, part in enumerate(parts):
        
        answer += my_strings[idx][part[0]:part[1]+1]
    return answer