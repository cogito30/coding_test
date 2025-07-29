# 최빈값 구하기
def solution(array):
    answer = 0
    countNum = dict()
    for i in array:
        if countNum.get(i):
            countNum[i] += 1
        else:
            countNum[i] = 1
    maxVal = max(list(countNum.values()))
    for k, v in countNum.items():
        if v == maxVal:
            if answer > 0:
                answer = -1
                break
            answer = k
        
    return answer