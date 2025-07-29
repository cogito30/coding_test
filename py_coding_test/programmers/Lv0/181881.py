# 조건에 맞게 수열 변환하기 2
def solution(arr):
    answer = 0
    while True:
        origin_arr = arr[::]
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] //= 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i] * 2 + 1
        answer += 1
        if origin_arr == arr:
            break
    return answer - 1