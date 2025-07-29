# 조건에 맞게 수열 변환하기 3
def solution(arr, k):
    answer = []
    if k % 2 == 1:
        answer = [i * k for i in arr]
    else:
        answer = [i + k for i in arr]
    return answer