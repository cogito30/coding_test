# 원소들의 곱과 합
def solution(num_list):
    answer = 0
    sumOfElement = sum(num_list)
    multiplyOfElement = 1
    for i in num_list:
        multiplyOfElement *= i
    if sumOfElement**2 > multiplyOfElement:
        answer = 1
    else:
        answer = 0
    return answer