# 배열의 길이를 2의 거듭제곱으로 만들기
def solution(arr):
    answer = [i for i in arr]
    lenArr = len(arr)
    count = 0
    while lenArr > 0:
        count += 1
        lenArr //= 2
    N = 0
    if len(arr) == 2 ** (count - 1):
        return answer
    for _ in range(2 ** count - len(arr)):
        answer.append(0)
    return answer