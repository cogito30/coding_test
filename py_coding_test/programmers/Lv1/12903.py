# 가운데 글자 가져오기
def solution(s):
    answer = ''
    lenStr = len(s)
    if lenStr % 2 == 0:
        answer = s[lenStr//2 - 1:lenStr//2 + 1]
    else:
        answer = s[lenStr//2]
    return answer