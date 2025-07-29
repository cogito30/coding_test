# 수열과 구간 쿼리 3
def solution(arr, queries):
    answer = []
    for query in queries:
        tmp = arr[query[0]]
        arr[query[0]] = arr[query[1]]
        arr[query[1]] = tmp
    answer = arr
    return answer