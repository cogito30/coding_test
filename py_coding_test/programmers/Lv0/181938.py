# 두 수의 연산값 비교하기
def solution(a, b):
    answer = 0
    num1 = int(str(a) + str(b))
    num2 = 2 * a * b
    if num1 >= num2:
        answer = num1
    else:
        answer = num2
    return answer