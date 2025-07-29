# 7의 개수
def solution(array):
    answer = 0
    for i in array:
        for j in str(i):
            if "7" == j:
                answer += 1
            
    return answer