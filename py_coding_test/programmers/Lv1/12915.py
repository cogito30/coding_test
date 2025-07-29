# 문자열 내 마음대로 정렬하기
def solution(strings, n):
    answer = []
    answer = sorted(strings, key=lambda x: (x[n], x))
    return answer