# 배열 만들기 5
def solution(intStrs, k, s, l):
    answer = []
    for strNum in intStrs:
        if int(strNum[s:s+l]) > k:
            answer.append(int(strNum[s:s+l]))
    return answer