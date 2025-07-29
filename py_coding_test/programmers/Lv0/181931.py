# 등차수열의 특정한 항만 더하기
def solution(a, d, included):
    answer = 0
    for idx, elem in enumerate(included):
        if elem:
            answer += (a + d*(idx))
    return answer