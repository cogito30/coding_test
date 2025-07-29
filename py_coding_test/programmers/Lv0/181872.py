# 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기
def solution(myString, pat):
    answer = ''
    
    idx = 0
    for i in range(len(myString)):
        if myString[i:i+len(pat)] == pat:
            idx = i
    answer = myString[:idx+len(pat)]
    return answer