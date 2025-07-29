# 체육복
def solution(n, lost, reserve):
    answer = 0
    # 반례 5, [1, 4], [2, 4] // 5
    cloth = [1 for _ in range(n+1)]
    cloth[0] = 0
    for i in range(1, n+1):
        if i in lost:
            cloth[i] -= 1
        if i in reserve:
            cloth[i] += 1

    
    print(cloth)
    
    for i in range(1, n):
        if cloth[i] == 0 and cloth[i-1] == 2:
            cloth[i] += 1
            cloth[i-1] -= 1
        if cloth[i] == 0 and cloth[i+1] == 2:
            cloth[i] += 1
            cloth[i+1] -= 1
            
    if cloth[n] == 0 and cloth[n-1] == 2:
        cloth[n] = 1
        cloth[n-1] -= 1

    for i in cloth:
        if i > 0:
            answer += 1
    print(cloth)
    return answer