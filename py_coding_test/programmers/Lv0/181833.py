# 특별한 이차원 배열 1
def solution(n):
    answer = []
    for i in range(n):
        answer.append([])
        for j in range(n):
            if j == i:
                answer[i].append(1)
            else:
                answer[i].append(0)
    return answer