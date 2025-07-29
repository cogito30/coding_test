# 하샤드 수
def solution(x):
    answer = False
    numberList = [int(i) for i in str(x)]
    if x % sum(numberList) == 0:
        answer = True
        
    return answer