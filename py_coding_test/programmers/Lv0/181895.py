# 배열 만들기 3
def solution(arr, intervals):
    answer = []
    for interval in intervals:
        answer.extend(arr[interval[0]:interval[1]+1])
    return answer