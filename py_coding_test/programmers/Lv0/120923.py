# 연속된 수의 합
def solution(num, total):
    answer = []
    # case: 5, 0, [-2, -1, 0, 1, 2] 확인
    for i in range(-total-num, total+num):
        sumNumber = 0
        for j in range(num):
            sumNumber += (i + j)
        if sumNumber == total:
            for j in range(num):
                answer.append(i + j)
    return answer