# 수열과 구간 쿼리 1
def solution(arr, queries):
    answer = []
    for s, e in queries:
        for i in range(s, e+1):
            arr[i] += 1
    answer = arr
    return answer