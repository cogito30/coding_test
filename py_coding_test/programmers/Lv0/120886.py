# A로 B 만들기
def solution(before, after):
    answer = 1
    beforeList = [i for i in before]
    afterList = [i for i in after]
    beforeList.sort()
    afterList.sort()
    for i in range(len(beforeList)):
        if beforeList[i] != afterList[i]:
            answer = 0
    return answer