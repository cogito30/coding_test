# 문자열 묶기
def solution(strArr):
    answer = 0
    result = [0 for _ in range(30)]
    for i in strArr:
        result[len(i)-1] += 1
    answer = max(result)
    return answer