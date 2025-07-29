# 문자열 내림차순으로 배치하기
def solution(s):
    answer = ''
    alphaList = [i for i in s]
    alphaList.sort(reverse=True)
    answer = ''.join(alphaList)
    return answer