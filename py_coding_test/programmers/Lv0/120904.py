# 숫자 찾기
def solution(num, k):
    answer = -1
    num = str(num)
    for idx, n in enumerate(num):
        if n == str(k):
            answer = idx + 1
            break
    return answer