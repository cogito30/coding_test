# 특별한 이차원 배열 2
def solution(arr):
    answer = 1
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != arr[j][i]:
                answer = 0
    return answer