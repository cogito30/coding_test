# 이어 붙인 수
def solution(num_list):
    answer = 0
    oddNum = ""
    evenNum = ""
    for i in num_list:
        if i % 2 == 1:
            oddNum += str(i)
        else:
            evenNum += str(i)
    answer = int(oddNum) + int(evenNum)
    return answer