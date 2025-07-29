# 최댓값과 최솟값
def solution(s):
    answer = ''
    sList = s.split(" ")
    numList = [int(i) for i in sList]
    minVal = min(numList)
    maxVal = max(numList)
    answer = f"{minVal} {maxVal}"
    return answer