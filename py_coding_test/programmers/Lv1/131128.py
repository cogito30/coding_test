# 숫자 짝꿍
def solution(X, Y):
    answer = ''
    x_count = [0 for _ in range(10)]
    y_count = [0 for _ in range(10)]
    
    for i in X:
        x_count[int(i)] += 1
    for j in Y:
        y_count[int(j)] += 1
    
    for i in range(9,-1,-1):
        if x_count[i] == 0 or y_count[i] == 0:
            continue 
        if x_count[i] < y_count[i]:
            for _ in range(x_count[i]):
                answer += str(i)
        elif x_count[i] >= y_count[i]:
            for _ in range(y_count[i]):
                answer += str(i)
                
    if len(answer) == 0:
        answer = "-1"
    elif answer[0] == "0" and len(answer) > 1:
        answer = "0"
    
    return answer