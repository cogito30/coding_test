# 2의 영역
def solution(arr):
    answer = []
    if 2 in arr:
        lIndex = arr.index(2)
        rIndex = len(arr) - (arr[::-1].index(2))
        answer = arr[lIndex:rIndex]
    else:
        answer = [-1]
    
    return answer