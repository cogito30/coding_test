# 배열 조각하기
def solution(arr, query):
    answer = []
    for i, q in enumerate(query):
        if i % 2 == 0:
            arr = arr[:q + 1]
        else:
            arr = arr[q:]
    answer = arr
    return answer