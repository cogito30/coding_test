# 무작위로 K개의 수 뽑기
def solution(arr, k):
    answer = []
    for i in range(len(arr)):
        if len(answer) < k and arr[i] not in answer:
            answer.append(arr[i])
    if len(answer) < k:
        for i in range(k-len(answer)):
            answer.append(-1)
    return answer