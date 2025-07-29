# 정사각형으로 만들기
def solution(arr):
    answer = []
    if len(arr) > len(arr[0]):
        for i in range(len(arr)):
            answer.append([])
            for j in range(len(arr[0])):
                answer[i].append(arr[i][j])
            for _ in range(len(arr) - len(arr[0])):
                answer[i].append(0)
    else:
        for i in range(len(arr[0])):
            answer.append([])
            for j in range(len(arr[0])):
                if i < len(arr):
                    answer[i].append(arr[i][j])
                else:
                    answer[i].append(0)
                    
    return answer