# 제일 작은 수 제거하기
def solution(arr):
    answer = arr[::]
    minVal = min(arr)
    answer.remove(minVal)
    if len(answer) == 0:
        answer.append(-1)
    return answer