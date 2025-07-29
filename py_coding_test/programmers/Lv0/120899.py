# 가장 큰 수 찾기
def solution(array):
    answer = []
    maxVal = max(array)
    maxValIndex = array.index(maxVal)
    answer = [maxVal, maxValIndex]
    return answer