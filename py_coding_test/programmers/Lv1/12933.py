# 정수 내림차순으로 배치하기
def solution(n):
    answer = 0
    numList = [i for i in str(n)]
    numList.sort(reverse=True)
    answer = int(''.join(numList))
    return answer