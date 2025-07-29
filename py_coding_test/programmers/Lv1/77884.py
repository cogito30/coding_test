# 약수의 개수와 덧셈
def check(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    if count % 2 == 0:
        return 1
    else:
        return -1
    
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        answer += check(i) * i
    
    return answer